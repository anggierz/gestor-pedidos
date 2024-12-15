from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import requests
import json
from linked_list import LinkedList
from bst import BST
from json_helpers import save_to_json
from typing import List

FILE_PRODUCTS = 'products.json'
FILE_ORDERS = 'orders.json'

products_bst = BST()
orders_ll = LinkedList()


app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float

class Order(BaseModel):
    id: int
    products: List[Product]
    

@app.post('/api/product')
def create_product(product: Product):
    existing_product = products_bst.search(product.id)
    if existing_product == None:
        products_bst.insert(product.id, product)
    else:
        raise HTTPException(status_code=404, detail= "A product with the same ID already exists")
    
    
    return {"response": "Product successfully created!", "Product": product}


@app.get('/api/product/{id}')
def get_product_by_id(id: int):
    existing_product = products_bst.search(id)
    if existing_product == None:
        raise HTTPException(status_code=404, detail=f"Product with ID {id} does not exist")
    
    return existing_product


@app.post('/api/order')
def create_order(order: Order):
    existing_order = orders_ll.find(order.id)
    
    if existing_order == None:
        
        orders_ll.add(order.id, order.products)
    else:
        raise HTTPException(status_code=404, detail=f"Order with ID {order.id} already exists.")
    
    #save_to_json(FILE_ORDERS, orders_ll.convert_to_list())
    
    return {"response": "Order successfully created!", "Order": order}


@app.get('/api/order/{id}')
def get_order_by_id(id: int):
    existing_order = orders_ll.find(id)
    if existing_order == None:
        raise HTTPException(status_code=404, detail=f"Order with ID {id} does not exist")  
    return existing_order

@app.post('/api/order/{id}')
def update_order(order: Order):
    existing_order = orders_ll.find(order.id)
    if existing_order == None:
        raise HTTPException(status_code=404, detail=f"Order with ID {id} does not exist")
    
    existing_order.products = order.products
    
    return {"response": "Order successfully updated!", "Order": order}
    
@app.delete('/api/order/{id}')
def delete_order(id: int):
    existing_order = orders_ll.find(id)
    
    if existing_order == None:
        raise HTTPException(status_code=404, detail=f"Order with ID {id} does not exist")
    
    orders_ll.delete(id)
    
    return  {"response": "Order successfully deleted!"}


@app.get('/api/order')
def get_all_orders():
    return orders_ll.printLL()


