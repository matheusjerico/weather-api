from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):
    city: str
    country: Optional[str] = "BR"
    state: Optional[str] = None
