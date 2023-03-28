from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from services import report_service

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/", include_in_schema=False)
async def index(request: Request):
    events = await report_service.get_reports()
    data = {"request": request, "events": events}
    return templates.TemplateResponse("home/index.html", data)


@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    return RedirectResponse(url="/static/img/favicon.ico")
