# Python ₘᵢₙᵢ capstone
# Weather API

import requests
import creds     #import external file (creds.py) which contains
                 # the API key with the variable "api_key". Keeps API key secret

base_url = "http://api.openweathermap.org/data/2.5/weather"
city = input("Enter city name: ")

requests_url = f"{base_url}?appid={creds.api_key}&q={city}" 
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"]
    print(weather[0]["description"])
    temperature = round(data["main"]["temp"] - 273.15, 2) * 9/5 + 32 #Converts Kelvin to Fahrenheit and rounds 
    print(f"Temperature: {temperature}")
else:
    print("Error")