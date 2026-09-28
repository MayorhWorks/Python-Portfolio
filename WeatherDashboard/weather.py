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



def main():
    while True:

        city = input("Enter City name (or "q" to quit): ").strip()

        if city.lower() == "q":
            print("Goodbye!!")
            break

        
        data = get_weather(city)

        if data:
            display_weather(data)
            

if __name__ == '__main__':
    main()
    

