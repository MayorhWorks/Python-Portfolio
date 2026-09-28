# Weather Dashboard (CLI)

A simple command-line weather application using the OpenWeatherMap API.

## Features

- Get current weather for any city
- Temperature, feels like, humidity, wind speed and description
- Secure API key using .env
- Good error handling (city not found, no internet, etc.)

## How to Run

1. Create a `.env` file and add:
   OPENWEATHER_API_KEY=your_api_key_here
2. Install requirements:
   pip install requests python-dotenv
3. Run:
   python weather.py
