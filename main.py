from fastapi import FastAPI, HTTPException, Body, Path
from pydantic import BaseModel
from typing import Dict
from linked_list import LinkedList
from bst import BST
from json_helpers import read_json, write_json

FILE_PRODUCTS = 'products.json'
FILE_ORDERS = 'orders.json'

#Models
class Product(BaseModel):
    id: int
    name: str
    price: float

class Order(BaseModel):
    id: int
    products: Dict[int, int] # {product_id and quantity of product}
    

#Initialize BST of Products
products_bst = BST()
#Load products from the JSON file into the BST
for product in read_json(FILE_PRODUCTS):
    products_bst.insert(product["id"], product)
    
#Initialize Linked List of Orders
orders_ll = LinkedList()
#Load orders from the JSON file into the BST
for order in read_json(FILE_ORDERS):
    orders_ll.add(order["id"], order)


#API
app = FastAPI()

# a) Create a product
@app.post('/api/product', tags=["PRODUCTS"], summary="Crear un producto",
         description="Este endpoint crea un producto y lo añade al BST y al JSON de base de datos.")
def create_product(product: Product = Body(..., description="El objeto Product que contiene los detalles del nuevo producto.")):
    products_bst.insert(product.id, product)
    products_json = read_json(FILE_PRODUCTS)
    products_json.append(product.dict())
    write_json(FILE_PRODUCTS, products_json)
    
    return {"response": "Product successfully created!", "Product": product}

# b) Get information about a product by id
@app.get('/api/product/{id}', tags=["PRODUCTS"], summary="Consultar información de un producto por ID",
         description="Este endpoint devuelve un producto a través de su ID.")
def get_product_by_id(id: int = Path(..., description="El ID único del producto que deseas obtener")):
    existing_product = products_bst.search(id)
    
    if existing_product == None:
        raise HTTPException(status_code=400, detail=f"Product with ID {id} does not exist")
    
    return existing_product

# c) Create a new order
@app.post('/api/order', tags=["ORDERS"], summary="Crear un nuevo pedido",
         description="Este endpoint crea un pedido y lo añade a la LL y a la base de datos JSON.")
def create_order(order: Order = Body(..., description="El objeto Order que contiene los detalles del nuevo pedido.")):
    orders_ll.add(order.id, order.dict())
    orders_json = read_json(FILE_ORDERS)
    orders_json.append(order.dict())
    write_json(FILE_ORDERS, orders_json)
    
    return {"response": "Order successfully created!", "Order": order}

# d) Get information about an order by id
@app.get('/api/order/{id}', tags=["ORDERS"], summary="Consultar información de un pedido por ID",
         description="Este endpoint devuelve un pedido a través de su ID.")
def get_order_by_id(id: int =  Path(..., description="El ID único del pedido que deseas obtener")):
    existing_order = orders_ll.find(id)
    if existing_order == None:
        raise HTTPException(status_code=400, detail=f"Order with ID {id} does not exist")  
    return existing_order

# e) Update an existing order
@app.post('/api/order/{id}', tags=["ORDERS"], summary="Actualizar un pedido existente",
         description="Este endpoint actualiza un pedido a través de su ID.")
def update_order(id: int =  Path(..., description="El ID único del pedido que deseas actualizar"),
                 order: Order = Body(..., description="El objeto Order que contiene los detalles del pedido a actualizar.")):
    existing_order = orders_ll.find(id)
    if existing_order == None:
        raise HTTPException(status_code=400, detail=f"Order with ID {id} does not exist")
    
    orders_json = read_json(FILE_ORDERS)
    existing_order["products"] = order.products
    
    for i, ord in enumerate(orders_json):
        if ord["id"] == id:
            orders_json[i]["products"] = order.products
            break
    
    write_json(FILE_ORDERS, orders_json)
    
    return {"response": "Order successfully updated!", "Order": order}

# f) Delete an order
@app.delete('/api/order/{id}', tags=["ORDERS"], summary="Eliminar un pedido",
         description="Este endpoint elimina un pedido a través de su ID.")
def delete_order(id: int  =  Path(..., description="El ID único del pedido que deseas eliminar")):
    existing_order = orders_ll.find(id)
    
    if existing_order == None:
        raise HTTPException(status_code=400, detail=f"Order with ID {id} does not exist")
    
    orders_ll.delete(id)
    #Save all orders that haven't been deleted in the json file
    orders_json = [ord for ord in read_json(FILE_ORDERS) if ord["id"] != id]
    write_json(FILE_ORDERS, orders_json)
    
    return  {"response": "Order successfully deleted!"}

# g) List all orders
@app.get('/api/order', tags=["ORDERS"], summary="Listar todos los pedidos",
         description="Este endpoint devuelve todos los pedidos.")
def get_all_orders():
    return orders_ll.convert_to_list()


