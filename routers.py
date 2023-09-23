from fastapi import APIRouter, HTTPException, Query, Request
from controllers import list_products, create_order, list_orders, get_order, update_product
from models import Product, Order, New_Quantity

# Create an instance of APIRouter for defining routes
router = APIRouter()

# Define an endpoint for the home page
@router.get("/")
async def home_page():
    """
    Endpoint to return a simple greeting message.

    Returns:
        str: A greeting message.
    """
    return "HELLO"

# Define an endpoint to get a list of products
@router.get("/products")
async def get_products():
    """
    Endpoint to retrieve a list of products.

    Returns:
        list: A list of product data.
    """
    return list_products()

# Define an endpoint to create an order
@router.post("/order")
async def post_order(order: Order):
    """
    Endpoint to create an order.

    Args:
        order (Order): The order data to create.

    Returns:
        dict: A response containing the order_id.
    """
    return {"order_id": create_order(order)}

# Define an endpoint to retrieve a list of orders with optional pagination parameters
@router.get("/orders")
async def get_orders(
    limit: int = Query(10, description="Number of items to return"),
    offset: int = Query(0, description="Offset for pagination")
):
    """
    Endpoint to retrieve a list of orders with optional pagination.

    Args:
        limit (int, optional): Number of items to return per page.
        offset (int, optional): Offset for pagination.

    Returns:
        dict: A response containing total_orders and a list of orders.
    """
    return list_orders(limit, offset)

# Define an endpoint to retrieve a single order by order_id
@router.get("/order/{order_id}")
async def get_single_order(order_id: str):
    """
    Endpoint to retrieve a single order by order_id.

    Args:
        order_id (str): The ID of the order to retrieve.

    Returns:
        Order: The order data.
    
    Raises:
        HTTPException: If the order is not found.
    """
    order = get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# Define an endpoint to update the quantity of a product by product_id
@router.put("/product/{product_id}")
async def put_product(product_id: str, new_quantity: New_Quantity):
    """
    Endpoint to update the quantity of a product by product_id.

    Args:
        product_id (str): The ID of the product to update.
        new_quantity (New_Quantity): The new quantity to set for the product.

    Returns:
        dict: A response message indicating the update status.
    
    Raises:
        HTTPException: If the product is not found.
    """
    if not update_product(product_id, new_quantity):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product updated successfully"}
