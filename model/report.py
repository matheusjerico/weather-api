from pydantic import BaseModel
from typing import Optional
from model.location import Location
from datetime import datetime


class ReportSubmittal(BaseModel):
    description: str
    location: Location


class Report(ReportSubmittal):
    id: str
    created_date: Optional[datetime]
