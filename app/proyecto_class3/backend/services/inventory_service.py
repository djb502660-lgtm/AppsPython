from sqlalchemy.orm import Session
from fastapi import HTTPException
from repositories.inventory_repository import InventoryRepository
from repositories.product_repository import ProductRepository
from schemas.inventory import InventoryMovementRequest
from models.inventory import InventoryTransaction
from models.user import User

class InventoryService:
    def __init__(self, db: Session):
        self.repo = InventoryRepository(db)
        self.prod_repo = ProductRepository(db)
        self.db = db

    def get_kardex(self, product_id: int):
        product = self.prod_repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return self.repo.get_by_product_id(product_id)

    def get_recent_movements(self):
        return self.repo.get_recent()

    def record_movement(self, request: InventoryMovementRequest, current_user: User):
        product = self.prod_repo.get_by_id(request.product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Producto no encontrado")

        previous_stock = product.stock
        new_stock = previous_stock
        
        # Calcular nuevo stock según el tipo de movimiento
        qty = request.quantity
        if request.transaction_type.value == "IN":
            new_stock += qty
        elif request.transaction_type.value == "OUT":
            if previous_stock < qty:
                raise HTTPException(status_code=400, detail="Stock insuficiente para la salida")
            new_stock -= qty
        elif request.transaction_type.value == "ADJUSTMENT":
            # Un ajuste fuerza el nuevo stock o puede ser interpretado como un delta.
            # En este diseño, trataremos ADJUSTMENT quantity como un delta, pero podría ser un valor absoluto.
            # Aquí lo sumamos/restamos según corresponda, o asumimos que quantity ya viene con signo si fuese permitido.
            # Por simplicidad del modelo (donde quantity es >0), un ajuste positivo sería un IN, pero
            # si se trata de 'fijar' un stock exacto, necesitaríamos redefinir. 
            # Asumiremos que ADJUSTMENT puede incrementar o decrementar según el caso en otra iteración, 
            # pero por ahora lo tratamos como entrada por mermas/sobrantes y requeriremos otro campo para dirección, 
            # o permitimos quantity negativos. Dado que Pydantic obliga gt=0, cambiaremos el request quantity temporalmente
            # a nivel lógico para este demo, o simplemente lo sumamos y en producción se expandiría.
            pass # Implementación simplificada: Para ajuste real se requeriría una dirección en el DTO.
            
            # Para hacer funcional la prueba: si es OUT usa OUT, si es IN usa IN. Ajuste requeriría más detalle.
            raise HTTPException(status_code=501, detail="Logica de ajustes pendiente de definicion direccional")

        # Actualizar producto
        product.stock = new_stock
        self.prod_repo.update(product)

        # Crear registro en Kardex
        transaction = InventoryTransaction(
            product_id=product.id,
            transaction_type=request.transaction_type.value,
            quantity=qty,
            previous_stock=previous_stock,
            new_stock=new_stock,
            reference=request.reference,
            notes=request.notes,
            created_by=current_user.id
        )
        
        return self.repo.create(transaction)
