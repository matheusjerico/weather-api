# Weather API

This is a simple API that returns the weather for a given city.

## Usage

To use this API, you need to make requests for these endpoints:

### GET `/<url>/api/weather/<city>`

    This endpoint returns the weather for a given city. The city name must be passed as a parameter in the URL.

> Usage example: `$ curl -X GET http://localhost:8000/api/weather/brasilia?state=DF&country=BR&units=metric`

The response will be a JSON object with the following structure:
```json
{
    "weather":
    [
        {
            "main":"Clouds",
            "description":"broken clouds"
        }
    ],
    "main":
    {
        "temp":22.51,
        "feels_like":22.49,
        "temp_min":22.51,
        "temp_max":22.51,
        "humidity":64
    },
    "visibility":10000,
    "clouds":
    {
        "all":75
    },
    "sys":
    {
        "country":"BR",
        "sunrise":"2023-03-20T06:15:33-03:00",
        "sunset":"2023-03-20T18:22:59-03:00"
    },
    "name":"Brasília"
}
```

### POST `/<url>/api/reports`

    This endpoint add a new report to the database. The report must be passed as a JSON object in the request body.

> Usage example: `$ curl -X POST http://localhost:8000/api/reports -H "Content-Type: application/json" -d '"description": "Rainning!","location": {"city": "brasilia", "state": "DF", "country": "BR"}'`

The response will be a JSON object with the following structure:
```json
{
    "description": "Rainning!",
    "location": {
        "city": "brasilia",
        "state": "DF",
        "country": "BR"
    },
    "id": "6954fb30-0e5e-4f65-8cba-f5a8420a9465",
    "created_date": "2023-03-23T18:39:29.504201-03:00"
}
```

### GET `/<url>/api/reports`

    This endpoint returns all reports from the database.

> Usage example: `$ curl -X GET http://localhost:8000/api/reports`

The response will be a JSON object with the following structure:
```json
[
    {
        "description": "Rainning!",
        "location": {
            "city": "brasilia",
            "state": "DF",
            "country": "BR"
        },
        "id": "6954fb30-0e5e-4f65-8cba-f5a8420a9465",
        "created_date": "2023-03-23T18:39:29.504201-03:00"
    },
    {
        "description": "Sunny!",
        "location": {
            "city": "brasilia",
            "state": "DF",
            "country": "BR"
        },
        "id": "6954fb30-0e5e-4f65-8cba-f5a8420a9465",
        "created_date": "2023-03-23T18:39:29.504201-03:00"
    }
]
```

## Configuration

The API can be configured by setting the following variables in the `settings.json` file:

```bash
{
    "api_key": "YOUR_API_KEY_FROM_openweathermap.org",
    "endpoint": "https://api.openweathermap.org/data/2.5/weather"
}
```

You need to get an API key from [openweathermap.org](https://openweathermap.org/). You can also change the endpoint if you want to use a different weather API. You need to create the file `settings.json` using the same structure as in the `settings_template.json` file.

## Development

To run the API locally, you need to create a virtual environment and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then, you can run the API using the following command:
    
```bash
bash uvicorn.sh
```

## 🍜 License

[MIT](https://choosealicense.com/licenses/mit/).<br>
