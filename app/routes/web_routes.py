from fastapi import APIRouter, Request, Form
from app.helpers.view_loader import render_view
from app.controllers.user_controller import create_user

router = APIRouter()

@router.get("/register")
def register(request: Request):
    return render_view(request, "form.html", {
        "message": ""
    })

@router.post("/users/create")
def user_create(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    create_user(name, email, password)

    return render_view(request, "form.html", {
        "message": "User created successfully 🎉"
    })