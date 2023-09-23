from pydantic import BaseModel
from typing import List
from datetime import datetime

class Product(BaseModel):
    """
    Pydantic model for representing a product.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        available_quantity (int): The available quantity of the product.
    """
    name: str
    price: float
    available_quantity: int

class UserAddress(BaseModel):
    """
    Pydantic model for representing a user's address.

    Attributes:
        city (str): The city of the user's address.
        country (str): The country of the user's address.
        zip_code (str): The ZIP code of the user's address.
    """
    city: str
    country: str
    zip_code: str

class OrderItem(BaseModel):
    """
    Pydantic model for representing an item in an order.

    Attributes:
        product_id (str): The ID of the product in the order.
        bought_quantity (int): The quantity of the product bought in the order.
    """
    product_id: str
    bought_quantity: int

class New_Quantity(BaseModel):
    """
    Pydantic model for representing a new quantity.

    Attributes:
        new_quantity (int): The new quantity value.
    """
    new_quantity : int

class Order(BaseModel):
    """
    Pydantic model for representing an order.

    Attributes:
        timestamp (str): The timestamp of the order (default is the current UTC time).
        items (List[OrderItem]): A list of OrderItem objects representing items in the order.
        user_address (UserAddress): The user's address associated with the order.
        total_amount (float): The total amount of the order (default is 0.0).
    """
    timestamp: str = str(datetime.utcnow())
    items: List[OrderItem]
    user_address: UserAddress
    total_amount: float = 0.0
