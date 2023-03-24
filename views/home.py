from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse("home/index.html", {"request": request})


@router.get("/favicon.ico")
def favicon():
    return RedirectResponse(url="/static/img/favicon.ico")
