import requests
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("Error: API key not found. Please check your .env file.")
    exit()


def get_weather(city:str):
    """Fetch current weather data for a given city"""

    if not city:
        print("City name cannot be empty.")
        return None 
    
    #build the url

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" #temperature in celsius
    }

    try:
        response = requests.get(base_url, params=param, timeout=10)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 404:
            print(f"City '{city}'not found. Please check the spelling")
            return None

        elif response.status_code == 401:
            print("Invalid API key. Please check your.env file.")
            return None

    except requests.exceptions.ConnectionError:
        print("No internet connection. Please check your network.")
        return None

    except requests.exceptions.Timeout:
        print("The request has timed out. Please try again")
        
    except Exception as e:
        print("An unexpected error occurred:", e)
        return None


def get_forecast(city:str):
    """Fetch 5-day / 3-hour forecast for a given city"""
    if not city:
        print("City name cannot be empty.")
        return None

    #build the url

    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    param = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try: 
        response = requests.get(base_url, params=param, timeout=10)

        if response.status_code == 200:
            return response.json()
        
        elif response.status_code == 404:
            print(f"City {city} not found. Please check the spelling")
            return None
        
        elif response.status_code == 401:
            print("Invalid API key. Please check your .env file.")
            return None

        else:
            print(f"Error {response.status_code}")
            return None


    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None



def display_weather(data:dict):
    """Display the weather information in a clean format"""
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"].capitalize()
    wind_speed = data["wind"]["speed"]

    print("\n====== Current Weather ======")
    print(f"City        : {city}, {country}")
    print(f"Condition   : {description}")
    print(f"Temperature : {temp}°C")
    print(f"Feels like  : {feels_like}°C")
    print(f"Humidity    : {humidity}%")
    print(f"Wind Speed  : {wind_speed} m/s")
    print("=============================")


def display_forecast(data:dict):
    """Display a simple 5-day forecast"""

    print("\n====== 5-Day Forecast ======")
    print(f"City: {data['city']['name']}, {data['city']['country']}\n")

    # We will show one summary per day (every 8th item ≈ 24 hours)
    # The API returns data every 3 hours, so 8 items = 24 hours

    forecast_list = data["list"]

    #group by date
    from collections import defaultdict
    daily = defaultdict(list)

    for item in forecast_list:
        date = item["dt_txt"].split[" "][0]   # get only the date part (YYYY-MM-DD)
        daily[date].append(item)

    for date, items in daily.items():
    # Take the midday forecast (around 12:00) if available, otherwise the first one
        midday = None
    for item in items:
        if "12:00:00" in item["dt_txt"]:
            midday = item
            break
    if not midday:
        midday = items[0]

    temp = midday["main"]["temp"]
    description = midday["weather"][0]["description"].capitalize()
    humidity = midday["main"]["humidity"]

    print(f"{date} → {temp}°C, {description}, Humidity: {humidity}%")

    print("============================")



def main():
    while True:
        print("\n1. Current Weather")
        print("2. 5-Day Forecast")
        print("3. Quit")
        
        choice = input("Choose an option (1-3): ").strip()

        if choice == "3":
            print("Goodbye!")
            break

        if choice not in ("1", "2"):
            print("Invalid choice.")
            continue

        city = input("Enter city name: ").strip()

        if choice == "1":
            data = get_weather(city)
            if data:
                display_weather(data)

        elif choice == "2":
            data = get_forecast(city)
            if data:
                display_forecast(data)

if __name__ == '__main__':
    main()
    

