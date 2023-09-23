from fastapi import FastAPI
from routers import router  # Import the router from the routers module

# Create an instance of the FastAPI application
app = FastAPI()

# Include the router in the FastAPI application
app.include_router(router)

# The FastAPI app is now ready to serve endpoints defined in the router

# Here's a breakdown of the code:

# 1. Import FastAPI and the router module where your routes are defined.

# 2. Create an instance of the FastAPI application using `FastAPI()` constructor.
#    This instance represents your FastAPI web application.

# 3. Include the router in the FastAPI application using `app.include_router(router)`.
#    This step integrates the routes defined in the router with the main application.
#    It means that all the routes defined in the router will be accessible under the root path of the application.
#    For example, if you have a route `/products` defined in the router, it will be accessible as `/products` in the application.

# 4. The FastAPI app is now ready to serve endpoints defined in the router.
