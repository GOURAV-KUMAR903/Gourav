from fastapi import APIRouter
from app.helpers.view_loader import render_view
from app.db.connection import get_conn

router = APIRouter()

@router.get("/")
def home():
    return render_view("index.html", {
        "message": "Hello Render 🚀"
    })


@router.get("/db-test")
def test_db():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    return {
        "status": "MySQL connected",
        "result": cursor.fetchone()
    }