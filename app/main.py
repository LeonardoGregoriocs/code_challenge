from fastapi import FastAPI

from app.config.routes import setup_routes

try:
    app = FastAPI()
    setup_routes(app)

except Exception as err:
    print(f"Error connecting with FastAPI: {err}")
