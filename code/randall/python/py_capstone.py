# Python ₘᵢₙᵢ capstone
# Weather API
import colorama
from colorama import Fore
import requests
import creds     #import external file (creds.py added to .gitignore) which contains
                 # the API key with the variable "api_key". Keeps API key secret

base_url = "http://api.openweathermap.org/data/2.5/weather"
city = input(Fore.GREEN +"Welcome to Weather Checker. For current conditions, please enter a city name: ")

requests_url = f"{base_url}?appid={creds.api_key}&q={city}" 
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"]
    print(Fore.YELLOW + weather[0]["description"].title())
    temperature = round(data["main"]["temp"] - 273.15) * 9/5 + 32 #Converts Kelvin to Fahrenheit and rounds 
    print(f"Temperature: {temperature} °f")
else:
    print("Error")