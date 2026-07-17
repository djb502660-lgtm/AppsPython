# SPEC 01: Architecture

## 1. Arquitectura Cliente Servidor
El sistema separa claramente la capa de presentación (Frontend) de la lógica de negocio y persistencia (Backend). El Frontend y el Backend se comunican exclusivamente a través de una API REST.

## 2. Arquitectura Modular
El backend se estructurará de forma modular, donde cada dominio del negocio (Usuarios, Productos, Pedidos, etc.) tendrá su propio módulo autocontenido, facilitando el mantenimiento y la escalabilidad.

## 3. Arquitectura Hexagonal y por Capas
Cada módulo del backend adoptará una estructura por capas para garantizar la separación de responsabilidades:

### 3.1. Controllers (Router / Endpoints)
Responsables de recibir las peticiones HTTP, parsear los datos de entrada, invocar a los servicios correspondientes y retornar las respuestas HTTP al cliente. No contienen lógica de negocio.

### 3.2. Services (Lógica de Negocio)
Contienen la lógica de negocio de la aplicación. Orquestan llamadas a repositorios, aplican reglas de negocio y manejan excepciones de dominio.

### 3.3. Repositories (Acceso a Datos)
Abstraen la lógica de acceso a la base de datos utilizando SQLAlchemy. Se encargan de las consultas, inserciones y actualizaciones. Aíslan a la capa de servicios de los detalles de persistencia.

### 3.4. DTOs (Data Transfer Objects / Pydantic Schemas)
Utilizados para validar y transferir datos entre las capas. En FastAPI, Pydantic se encarga de definir los DTOs de entrada (Requests) y salida (Responses).

### 3.5. Entities (SQLAlchemy Models)
Representan las tablas de la base de datos y sus relaciones. Son el núcleo del ORM.

## 4. Flujo de Petición
1. **Cliente** hace petición HTTP al **Controller**.
2. **Controller** valida la entrada mediante **DTOs** (Pydantic).
3. **Controller** llama al **Service** pasándole los datos validados.
4. **Service** ejecuta la lógica y llama al **Repository**.
5. **Repository** interactúa con la Base de Datos mediante **Entities** (SQLAlchemy).
6. Los datos retornan por la cadena y el **Controller** emite la respuesta HTTP final formateada según el **DTO** de salida.
