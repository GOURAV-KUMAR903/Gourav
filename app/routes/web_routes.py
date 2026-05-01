from fastapi import APIRouter
from app.helpers.view_loader import render_view
from app.db import cursor  # 👈 IMPORTANT

router = APIRouter()

@router.get("/")
def home():
    return render_view("index.html", {
        "message": "Hello Render 🚀"
    })

@router.get("/db-test")
def test_db():
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    return {
        "status": "DB connected",
        "result": result
    }