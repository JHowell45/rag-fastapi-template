from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api import router

app = FastAPI()
app.include_router(router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def redirect_to_docs(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="index.html", context={})
