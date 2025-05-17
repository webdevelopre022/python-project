import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Error:", data.get("message", "Unable to fetch weather data."))

# Example usage
API_KEY = 'your_openweathermap_api_key'  # Replace with your actual API key
city_name = input("Enter city name: ")
get_weather(city_name, API_KEY)

"""Get an API Key
Sign up at https://openweathermap.org/ and get your free API key."""
