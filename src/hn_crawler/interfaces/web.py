# src/hn_crawler/interfaces/web.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from hn_crawler.application.service import list_entries
from hn_crawler.interfaces.api import router as api_router

AUTHOR = ("Andrés Núñez")
ROLE   = ("Full Stack Developer")
EMAIL  = ("Andriu_red@hotmail.com")


app = FastAPI(title="HN Crawler")
app.include_router(api_router, prefix="/api")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request, filter: str | None = None):
    return templates.TemplateResponse(
    "index.html",
    {
        "request": request,
        "entries": list_entries(filter),
        "current": filter,
        "author": AUTHOR,
        "role": ROLE,
        "email": EMAIL,
    },
)

