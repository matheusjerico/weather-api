from datetime import datetime
from typing import List
from model.report import Report, ReportSubmittal
from model.location import Location
from pytz import timezone
from uuid import uuid4

__reports: List[Report] = []


async def get_reports() -> List[Report]:
    """
    Get all reports

    Returns:
        List[Report]: All reports
    """

    # would be an async call here
    return list(__reports)


async def add_report(report_submittal: ReportSubmittal) -> Report:
    """
    Add a report

    Args:
        report_submittal (ReportSubmittal): Report to be added

    Returns:
        Report: The report added

    """
    now = datetime.now(tz=timezone("America/Sao_Paulo"))
    report = Report(
        id=str(uuid4()),
        description=report_submittal.description,
        location=report_submittal.location,
        created_date=now,
    )

    # would be an async call here
    # simulate how to save in a database
    # we need to change it to use a mysql instance
    __reports.append(report)
    __reports.sort(key=lambda x: x.created_date, reverse=True)

    return report
