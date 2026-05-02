import os
from fastapi.templating import Jinja2Templates

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "views", "templates")
)

def render_view(request, template_name: str, context: dict = None):
    context = context or {}

    return templates.TemplateResponse(template_name, {
        "request": request,
        **context
    })