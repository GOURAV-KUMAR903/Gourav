from fastapi import APIRouter
from app.helpers.view_loader import render_view

router = APIRouter()

@router.get("/")
def home():
    return render_view("index.html", {
        "message": "Hello Render 🚀"
    })

@router.get("/db-test")
def test_db():
    cursor.execute("SELECT 1")
    return {"status": "DB connected"}

