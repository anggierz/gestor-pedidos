# Sistema de gestión de pedidos

## Descripción del proyecto

Este repositorio incluye la actividad 2: Uso de estructuras de datos avanzadas del Módulo 2. Fundamentos de Backend con Python
del Máster de Desarrollo Web de la UEM.

Se implementa un sistema de gestión de pedidos para una tienda en línea que permite la creación, actualización, eliminación
y consulta de pedidos utilizando una API RESTful. Los pedidos estarán compuestos por
múltiples productos, y cada producto tendrá su propia información detallada. Se
utilizarán estructuras de datos avanzadas para gestionar los productos y los pedidos, y
se implementarán técnicas de serialización y deserialización para el manejo de datos

## Funcionalidades

1. **Gestión de Productos**:
   - Crear y consultar información de productos.
   - Los productos  tienen los siguientes atributos definidos en el modelo de datos: id, name, price.

2. **Gestión de pedidos**:
   - Crear, consultar, actualizar y eliminar pedidos.
   - Los pedidos  tienen los siguientes atributos definidos en el modelo de datos: id, y lista de productos: id y cantidad.


## Endpoints disponibles

Podrás encontrar más información sobre los endpoints documentado en Swagger en la siguiente ruta: http://127.0.0.1:8000/docs#/


### **1. Gestión de Productos (PRODUCTS)**

#### **GET /api/product/{id}**

#### **POST /api/product**

### **2. Gestión de Pedidos (ORDERS)**

#### **GET /api/order**

#### **POST /api/order**

#### **GET /api/order/{id}**

#### **POST /api/order/{id}**

#### **DELETE /api/order/{id}**

## Instrucciones de uso

### 1. Clonar el Repositorio

Primero, clona el repositorio del proyecto a tu máquina local

### 2. Instalar dependencias 

Instala las dependencias que se encuentran en el archivo requirements.txt

```bash
pip install -r requirements.txt
```

### 3. Levantar los endpoints

Finalmente, levanta las rutas para poder utilizarlas

```bash
uvicorn main:app --reload
```
