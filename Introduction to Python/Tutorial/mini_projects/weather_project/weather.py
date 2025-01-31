from dotenv import load_dotenv
from pprint import pprint
import requests, os

load_dotenv()

def get_current_weather(city='Berlin'):
    
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&lang=en&units=metric"
    
    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == '__main__':
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only space
    if not bool(city.strip()):
        city = 'Berlin'
    
    weather_data = get_current_weather(city)

    print('\n')
    pprint(weather_data)
