import requests
import sys

sys.path.append("../")

from model.report import ReportSubmittal
from model.location import Location


def main():
    """
    This is a app to ask what user would like to see.
    """

    choice = input("[R]eport weather or [s]ee reports? ")

    while choice:
        if choice.lower() == "r":
            report_weather()
        elif choice.lower() == "s":
            see_reports()
        else:
            print("Invalid choice. Please try again.")

        choice = input("[R]eport weather or [s]ee reports? ")


def report_weather():
    """
    This is a app to report weather.
    """
    description = input("What is happening now: ")
    city = input("What city: ")

    report = ReportSubmittal(
        description=description,
        location=Location(city=city),
    )

    r = requests.post("http://127.0.0.1:8000/api/reports", json=report.dict())
    r.raise_for_status()
    data = r.json()

    print(f"Report sent successfully: {data.get('id')}")


def see_reports():
    """
    This is a app to see reports.
    """
    url = "http://127.0.0.1:8000/api/reports"
    r = requests.get(url)
    r.raise_for_status()

    reports = r.json()

    for r in reports:
        print(f"{r.get('location').get('city')} has {r.get('description')}")


if __name__ == "__main__":
    main()
