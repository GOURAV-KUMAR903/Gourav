import os
from fastapi.responses import HTMLResponse

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def render_view(template_name: str, context: dict = None) -> HTMLResponse:
    context = context or {}

    file_path = os.path.join(BASE_DIR, "views", "templates", template_name)

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # SIMPLE VARIABLE REPLACEMENT (NO JINJA)
    for key, value in context.items():
        html = html.replace(f"{{{{ {key} }}}}", str(value))

    return HTMLResponse(content=html)