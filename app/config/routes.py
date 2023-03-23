from fastapi import FastAPI

from app.routes import routes

def setup_routes(app: FastAPI):
    app.include_router(routes.router,
        prefix="/calculate",
        tags= ['Calculate Quantity Ink']
    )
