# E-Commerce API

This project is an example of a simple E-Commerce API built using FastAPI and MongoDB. It provides endpoints to manage products and orders in an e-commerce application.

## Table of Contents

- [Code Structure](#code-structure)
- [Code Explanation](#code-explanation)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)

## Code Structure

The code is organized into several files to maintain a clean and structured project:

- **models.py**: Defines data models using Pydantic, including `Product`, `UserAddress`, `OrderItem`, `New_Quantity`, and `Order`.

- **controllers.py**: Contains controller functions for core business logic, such as listing products, creating orders, listing orders, getting order details, and updating product quantities.

- **routers.py**: Defines API endpoints using FastAPI's `APIRouter` and maps HTTP methods to controller functions.

- **main.py**: The entry point of the FastAPI application. It initializes the app, includes routers, and sets up the MongoDB database connection.

- **.env**: Stores environment variables, such as the database URL.

## Code Explanation

1. **MongoDB Setup**: The application connects to a MongoDB database using the `pymongo` library, with the database URL stored in the `.env` file.

2. **Data Models**: Data models are defined using Pydantic for data validation and serialization. Models include `Product`, `UserAddress`, `OrderItem`, `New_Quantity`, and `Order`.

3. **Controllers**: `controllers.py` contains core logic, including functions like `list_products()`, `calculate_order_total(order)`, `create_order(order)`, `list_orders(limit, offset)`, `get_order(order_id)`, and `update_product(product_id, new_quantity)`.

4. **Routers**: `routers.py` defines API endpoints using FastAPI's `APIRouter`. Endpoints include listing products, creating orders, listing orders with pagination, getting order details, and updating product quantities.

5. **GET Requests**: GET requests retrieve data, such as listing products or orders, with optional pagination parameters.

6. **POST Request**: POST requests create new orders, with the request body containing order details in JSON format.

7. **PUT Request**: PUT requests update the quantity of a product, with the request body containing the new quantity.

8. **Error Handling**: Error handling is implemented using FastAPI's `HTTPException`. For example, if an order is not found, a 404 error is returned.

9. **Environmental Variables**: Sensitive information like the database URL is stored in environment variables using the `.env` file.

## Getting Started

To run this project locally, follow these steps:

1. Clone this repository to your local machine.

2. Install the required dependencies using `pip install -r requirements.txt`.

3. Create a `.env` file with the following content:


Replace `DATABASE_URL655555555 ` with your MongoDB connection string.

4. Run the FastAPI application using `uvicorn main:app --reload`.

5. Access the API at `http://localhost:8000` in your web browser or use a tool like Postman to make API requests.

## API Endpoints

- **GET /products**: List all products.
- **POST /order**: Create a new order.
- **GET /orders**: List orders
- **GET /orders?limit=4&offset=4**: List orders with pagination. limit defines how many orders to show and offset defines how many orders to skip to show the repsonse.
- **GET /order/{order_id}**: Get details of a specific order.
- **PUT /product/{product_id}**: Update the quantity of a product.
