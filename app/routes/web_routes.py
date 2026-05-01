from fastapi import APIRouter
from app.helpers.view_loader import render_view
from app.db import connection

router = APIRouter()

@router.get("/")
def home():
    return render_view("index.html", {
        "message": "Hello Render 🚀"
    })

@router.get("/db-test")
def test_db():
    connection.cursor.execute("SELECT 1")
    return {
        "status": "DB connected",
        "result": connection.cursor.fetchone()
    }