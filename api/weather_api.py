from fastapi import APIRouter, Response
from fastapi import Depends
from typing import Optional
from typing import List
from model.location import Location
from model.report import Report, ReportSubmittal
from services import openweather_service
from services import report_service
from model.validation_error import ValidationError


router = APIRouter()


@router.get("/api/weather/{city}", name="Get weather for a city")
async def weather(loc: Location = Depends(), units: Optional[str] = "metric"):
    """
    Endpoint for getting weather data for a given city.

    :param loc: Location object
    :param units: Units for temperature
    :return: Response object
    """
    try:
        return await openweather_service.get_report_async(
            loc.city, loc.state, loc.country, units
        )

    except ValidationError as ve:
        return Response(content=ve.error_message, status_code=ve.status_code)

    except Exception as e:
        print(f"Server crashed: {e}")
        return Response(content=str(e), status_code=500)


@router.get("/api/reports", name="Get all reports")
async def reports_get() -> List[Report]:
    """
    Endpoint for getting all reports

    :return: List of reports
    """
    return await report_service.get_reports()


@router.post("/api/reports", name="Add reports", status_code=201)
async def report_post(report: ReportSubmittal) -> Report:
    """
    Endpoint for adding a report

    :param report: ReportSubmittal object
    :return: Report object
    """

    return await report_service.add_report(report_submittal=report)
