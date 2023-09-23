from pymongo import MongoClient
from bson import ObjectId
from models import Product, Order, OrderItem, New_Quantity
import json
from fastapi import Request, Query
from starlette.config import Config

# Load configuration from .env file
config = Config('.env')
DATABASE_URL = config("DATABASE_URL")

# Connect to the MongoDB database
client = MongoClient(DATABASE_URL)
db = client["ecommerce_db"]
products_collection = db["products"]
orders_collection = db["orders"]

def list_products():
    """
    Retrieve a list of products from the database.

    Returns:
        str: A JSON-encoded string representing the list of products.
    """
    products = list(products_collection.find())
    return str(products)

def calculate_order_total(order: Order):
    """
    Calculate the total amount of an order based on its items and product prices.

    Args:
        order (Order): The order for which to calculate the total amount.

    Returns:
        float: The total order amount.
    """
    total_amount = 0.0
    for item in order.items:
        product = products_collection.find_one({"_id": ObjectId(item.product_id)})
        if product:
            total_amount += float(product["price"]) * item.bought_quantity
    return total_amount

def create_order(order: Order):
    """
    Create a new order in the database and update product quantities.

    Args:
        order (Order): The order data to create.

    Returns:
        str: The ID of the newly created order.
    
    Raises:
        str: If there is not enough quantity available for a product.
    """
    total_amount = calculate_order_total(order)
    
    # Update the order's total_amount field
    order.total_amount = total_amount
    
    # Update product quantities based on items in the order
    for item in order.items:
        product_id = item.product_id
        bought_quantity = item.bought_quantity
        product = products_collection.find_one({"_id": ObjectId(product_id)})
        if product:
            # Calculate the new available_quantity
            new_quantity = int(product["available_quantity"]) - bought_quantity
            if new_quantity >= 0:
                # Update the product's available_quantity in the database
                products_collection.update_one(
                    {"_id": ObjectId(product_id)},
                    {"$set": {"available_quantity": new_quantity}}
                )
            else:
                return "Not enough quantity available for product: " + product_id
    
    order_data = order.dict()
    order_id = orders_collection.insert_one(order_data).inserted_id
    return str(order_id)

def list_orders(limit: int = Query(10, description="Number of items to return"), offset: int = Query(0, description="Offset for pagination")):
    """
    Retrieve a list of orders from the database with optional pagination.

    Args:
        limit (int, optional): Number of items to return per page.
        offset (int, optional): Offset for pagination.

    Returns:
        str: A JSON-encoded string representing total_orders and a list of orders.
    """
    total_orders = orders_collection.count_documents({})
    orders = list(orders_collection.find().skip(offset).limit(limit))
    return str({"total_orders": total_orders, "orders": orders})

def get_order(order_id: str):
    """
    Retrieve a single order by order_id from the database.

    Args:
        order_id (str): The ID of the order to retrieve.

    Returns:
        str: A JSON-encoded string representing the order data.
    
    Raises:
        str: If the order is not found.
    """
    order = orders_collection.find_one({"_id": ObjectId(order_id)})
    if order is None:
        return "Order not found"
    return str(order)

def update_product(product_id: str, new_quantity: New_Quantity):
    """
    Update the quantity of a product by product_id in the database.

    Args:
        product_id (str): The ID of the product to update.
        new_quantity (New_Quantity): The new quantity to set for the product.

    Returns:
        bool: True if the product was updated successfully, False if not found.
    """
    result = products_collection.update_one({"_id": ObjectId(product_id)}, {"$set": {"available_quantity": new_quantity.new_quantity}})
    return result.matched_count > 0
