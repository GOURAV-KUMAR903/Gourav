from fastapi import APIRouter,Form
from app.helpers.view_loader import render_view
from app.db.connection import get_conn
from app.controllers.user_controller import create_user
from fastapi.responses import RedirectResponse
from fastapi import Request

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
    
@router.get("/register")
def register(request: Request):
    success = request.query_params.get("success")

    message = ""
    if success:
        message = "User created successfully 🎉"

    return render_view("form.html", {
        "message": message
    })

@router.post("/users/create")
def user_create(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    create_user(name, email, password)
    return RedirectResponse(url="/register?success=1", status_code=303)