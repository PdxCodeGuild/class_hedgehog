# Python ₘᵢₙᵢ capstone
# UV index and Weather API
# Weather  ---  https://openweathermap.org/api
# UV Index ---  https://data.epa.gov/efservice/getEnvirofactsUVDAILY/ZIP

from sre_parse import State
from colorama import Fore  # for purdy colors
import requests
import creds     #import external file (creds.py added to .gitignore) which contains
                 # the API key with the variable "api_key". Keeps API key secret

def weather():      # Not getting accurate weather data
    """This function will return the general weather conditions of the entered city"""

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    city = input(Fore.GREEN +"Welcome to Weather Checker. For current conditions, please enter a city name: ")
    state = input(Fore.GREEN +"Please enter the state: ")
    requests_url = f"{base_url}?q={city},{state},USA&appid={creds.api_key}"
    response = requests.get(requests_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"]
        print(Fore.YELLOW + weather[0]["description"].title())
        temperature = round(data["main"]["temp"] - 273.15) * 9/5 + 32 #Converts Kelvin to Fahrenheit and rounds 
        print(f"Temperature: {temperature} °f")
    else:
        print("Error")

def uv_index():
    """This function will return the UV index of the entered zip code"""

    zip_code = input(Fore.GREEN +"Please enter the Zip Code: ")
    requests_url = f"https://data.epa.gov/efservice/getEnvirofactsUVDAILY/ZIP/{zip_code}/JSON"
    response = requests.get(requests_url)
    
    if response.status_code == 200:
        data = response.json()
        zip = data[0]["ZIP_CODE"]              
        uv = data[0]["UV_INDEX"]
        uv_alert = data[0]["UV_ALERT"]
        print(f"For zip code {zip}, the UV index is {uv} and the UV alert level is {uv_alert}")
        uv = int(uv)
        if uv <= 2:
           print(Fore.GREEN + "UV index is low. Enjoy your day!")
        elif uv <= 5:
              print(Fore.YELLOW + "UV index is moderate. Enjoy your day!")
        elif uv <= 7:                                                           #change these
                print(Fore.RED + "UV index is high. Enjoy your day!")
        elif uv <= 10:
                print(Fore.RED + "UV index is very high. Enjoy your day!")
        elif uv >= 11:
                print(Fore.RED + "UV index is extreme. Enjoy your day!")
        
        
    else:
        print("Error")

user_input = input(Fore.GREEN + "Welcome to Weather & UV index Checker. Would you like to see the UV index (u) or weather (w)? (u/w): ").lower()

if user_input == "w":
    weather()
elif user_input == "u":
    uv_index()