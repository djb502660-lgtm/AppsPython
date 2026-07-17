from sqlalchemy.orm import Session
from core.database import SessionLocal, engine, Base
from models.role import Role, Permission
from models.user import User
from models.product import Category, Product
from core.security import get_password_hash

def init_db():
    db = SessionLocal()
    
    # Check if we already have roles
    if db.query(Role).first():
        print("Database already seeded. Skipping.")
        db.close()
        return

    print("Seeding database...")

    # 1. Permisos Base (CRUD simple para módulos principales)
    perms = [
        "users:MANAGE",
        "roles:MANAGE",
        "products:CREATE", "products:UPDATE", "products:DELETE",
        "inventory:MANAGE", "inventory:READ",
        "orders:UPDATE_STATUS", "orders:READ_ALL",
        "billing:MANAGE"
    ]
    db_perms = [Permission(name=p, module=p.split(":")[0]) for p in perms]
    db.add_all(db_perms)
    db.commit()

    # 2. Roles
    role_admin = Role(name="Super Admin", description="Acceso total al sistema")
    role_admin.permissions = db.query(Permission).all()
    
    role_cocina = Role(name="Cocina", description="Gestión de preparación de pedidos")
    role_cocina.permissions = db.query(Permission).filter(Permission.name.in_(["orders:UPDATE_STATUS", "orders:READ_ALL", "inventory:READ"])).all()
    
    role_cajero = Role(name="Cajero", description="Cobros y facturación")
    role_cajero.permissions = db.query(Permission).filter(Permission.name.in_(["orders:UPDATE_STATUS", "orders:READ_ALL", "billing:MANAGE"])).all()
    
    role_cliente = Role(name="Cliente", description="Usuario final de la plataforma")
    
    db.add_all([role_admin, role_cocina, role_cajero, role_cliente])
    db.commit()

    # 3. Usuario Super Admin
    admin_user = User(
        email="admin@fastfood.com",
        password_hash=get_password_hash("Admin123*"),
        first_name="Administrador",
        last_name="Principal",
        role_id=role_admin.id,
        is_active=True
    )
    db.add(admin_user)
    db.commit()

    # 4. Categorías
    cat_promos = Category(name="Promos", description="Combos y ofertas especiales")
    cat_hamburguesas = Category(name="Hamburguesas", description="Hamburguesas a la parrilla")
    db.add_all([cat_promos, cat_hamburguesas])
    db.commit()

    # 5. Productos Demo
    p1 = Product(
        name="Doble Burger Bacon", 
        description="Doble carne, queso cheddar, tocino ahumado y salsa especial.", 
        price=12.50, stock=50, category_id=cat_hamburguesas.id
    )
    p2 = Product(
        name="Combo Smash + Papas", 
        description="Smash burger con papas grandes y gaseosa.", 
        price=15.00, stock=30, category_id=cat_promos.id
    )
    db.add_all([p1, p2])
    db.commit()

    print("Seeding completed successfully!")
    db.close()

if __name__ == "__main__":
    init_db()
