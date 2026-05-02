import os
from fastapi.responses import HTMLResponse

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def render_view(template_name: str, context: dict = None) -> HTMLResponse:
    context = context or {}

    file_path = os.path.join(BASE_DIR, "views", "templates", template_name)

    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    message = context.get("message")

    if message:
        context["message_html"] = f"""
        <div class="alert alert-success text-center">
          {message}
        </div>
        """
    else:
        context["message_html"] = ""

    # SIMPLE VARIABLE REPLACEMENT
    for key, value in context.items():
        html = html.replace(f"{{{{ {key} }}}}", str(value))

    return HTMLResponse(content=html)