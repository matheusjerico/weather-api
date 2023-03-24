from typing import List
from pydantic import validator, BaseModel
from datetime import datetime
from pytz import timezone


class WeatherItem(BaseModel):
    main: str
    description: str


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    humidity: int


class Clouds(BaseModel):
    all: int


class Sys(BaseModel):
    country: str
    sunrise: int
    sunset: int

    @validator("sunrise")
    def sunrise_to_datetime(cls, val: int) -> datetime:
        return datetime.fromtimestamp(val, tz=timezone("America/Sao_Paulo"))

    @validator("sunset")
    def sunset_to_datetime(cls, val: int) -> datetime:
        return datetime.fromtimestamp(val, tz=timezone("America/Sao_Paulo"))


class WeatherResponse(BaseModel):
    weather: List[WeatherItem]
    main: Main
    visibility: int
    clouds: Clouds
    sys: Sys
    name: str
