# Python ₘᵢₙᵢ capstone
# Weather API

from colorama import Fore  # for purdy colors
import requests
import creds     #import external file (creds.py added to .gitignore) which contains
                 # the API key with the variable "api_key". Keeps API key secret

def general_conditions():
    """This function will return the general conditions of the selected city"""

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


def detailed_conditions():
    """This function will return the detailed conditions of the weather.""" #REQUIRES A PAID API KEY

    lat = input(Fore.GREEN +"Enter latitude: ")
    lon = input(Fore.GREEN +"Enter longitude: ")
    requests_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={creds.api_key}"
    

    #requests_url = f"{base_url}?appid={creds.api_key}&q={city}" 
    response = requests.get(requests_url)

    print(response)
"""
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"]
        print(Fore.YELLOW + weather[0]["description"].title())
        temperature = round(data["main"]["temp"] - 273.15) * 9/5 + 32 #Converts Kelvin to Fahrenheit and rounds 
        print(f"Temperature: {temperature} °f")
    else:
        print("Error")
"""  

user_input = input(Fore.GREEN + "Welcome to Weather Checker. Would you like to see the general or the detailed conditions? (g/d): ").lower()

if user_input == "g":
    general_conditions()
elif user_input == "d":
    detailed_conditions()