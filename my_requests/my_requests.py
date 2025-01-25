import requests

API_KEY = 'ce61fc5d32bd08550ebbaaadcf9bd46f'
city_name = input("Enter your city: ")
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'

try:
    response = requests.get(url)
    response.raise_for_status()  

    data = response.json()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    weather_description = data['weather'][0]['description']

    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {weather_description.capitalize()}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except KeyError:
    print("Invalid response structure. Please check the city name or API response.")
