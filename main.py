import uvicorn
import json
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
from pathlib import Path
from api import weather_api
from views import home
from utils import variables


api = FastAPI()


def configure():
    """
    Configure the application.
    """
    configure_routing()
    configure_api_keys()


def configure_routing():
    """
    Configure routing for the application.
    """
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(home.router)
    api.include_router(weather_api.router)


def configure_api_keys():
    """
    Configure API keys for the application.
    """
    settings_file = Path("settings.json").absolute()
    if settings_file.exists():
        with open(settings_file, "r") as f:
            settings = json.load(f)
            variables.api_key = settings.get("api_key")
            variables.endpoint = settings.get("endpoint")
    else:
        raise FileNotFoundError("settings.json file not found.")


if __name__ == "__main__":
    """
    This is executed when the application is executed using
    python command line.
    """
    configure()
    uvicorn.run(api, host="127.0.0.1", port=8000, reload=True)

else:
    """
    This is executed when the application is executed using
    uvicorn command line.
    """
    configure()
