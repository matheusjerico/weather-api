import httpx
from typing import Optional, Tuple
from utils import variables
from model.weather import WeatherResponse
from fastapi.exceptions import RequestValidationError
from infraestructure import weather_cache
from model.validation_error import ValidationError


async def get_report_async(
    city: str, state: Optional[str], country: str, units: str
) -> WeatherResponse:
    """
    Get the weather report for the specified city, state, country, and units.

    :param city: The city to get the weather report for.
    :param state: The state to get the weather report for.
    :param country: The country to get the weather report for.
    :param units: The units to get the weather report for.
    :return: The weather report for the specified city, state, country, and units.
    """
    city, state, country, units = validate_units(city, state, country, units)

    if weather := weather_cache.get_weather(
        city=city, state=state, country=country, units=units
    ):
        return weather

    if state:
        q: str = f"{city},{state},{country}"
    else:
        q: str = f"{city},{country}"

    url: str = (
        f"{variables.endpoint}?q={q}&appid={variables.api_key}&units={units}"
    )

    async with httpx.AsyncClient() as client:
        r: httpx.Response = await client.get(url)
        if r.status_code != 200:
            raise ValidationError(
                error_message=r.text,
                status_code=r.status_code,
            )

        weather = WeatherResponse.parse_obj(r.json())
        weather_cache.set_weather(
            city=city, state=state, country=country, units=units, value=weather
        )
        return weather


def validate_units(
    city: str, state: Optional[str], country: str, units: str
) -> Tuple[str, Optional[str], str, str]:
    """
    Validate the units.

    :param city: The city to validate the units for.
    :param state: The state to validate the units for.
    :param country: The country to validate the units for.
    :param units: The units to validate.
    :return: None
    """

    city = city.strip().lower()

    if not country:
        country = "br"
    else:
        country = country.strip().lower()

    if len(country) != 2:
        error = f"Country must be a two-letter ISO 3166-1 code. {country} is not valid."
        raise ValidationError(
            error_message=error,
            status_code=400,
        )

    if state:
        state = state.strip().lower()

    if state and len(state) != 2:
        error = f"State must be a two-letter ISO 3166-1 code. {state} is not valid."
        raise ValidationError(
            error_message=error,
            status_code=400,
        )

    if units:
        units = units.strip().lower()

    valid_units = ["metric", "imperial", "standard"]
    if units not in valid_units:
        raise ValidationError(
            error_message=f"Units must be one of {valid_units}",
            status_code=400,
        )

    return city, state, country, units
