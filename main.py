from fastapi import FastAPI
from app.routes.web_routes import router as web_router

app = FastAPI()

app.include_router(web_router)