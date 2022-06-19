# Python ₘᵢₙᵢ capstone
# UV index and Weather API
# Weather  ---  https://openweathermap.org/api
# UV Index ---  https://data.epa.gov/efservice/getEnvirofactsUVDAILY/ZIP

from colorama import Fore  # for purdy colors
import requests
import creds     #import external file (creds.py added to .gitignore) which contains
                 # the API key with the variable "api_key". Keeps API key secret

def weather():
    """This function will return the general weather conditions of the entered city"""

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

def uv_index():
    """This function will return the UV index of the entered zip code"""

    zip_code = input(Fore.GREEN +"Please enter the Zip Code: ")
    requests_url = f"https://data.epa.gov/efservice/getEnvirofactsUVDAILY/ZIP/{zip_code}/JSON"
    response = requests.get(requests_url)
    
    if response.status_code == 200:
        data = response.json()
        zip = data[0]["ZIP_CODE"]              
        UV = data[0]["UV_INDEX"]
        UV_ALERT = data[0]["UV_ALERT"]
        print(zip)
        
    else:
        print("Error")

user_input = input(Fore.GREEN + "Welcome to Weather & UV index Checker. Would you like to see the UV index (u) or weather (w)? (u/w): ").lower()

if user_input == "w":
    weather()
elif user_input == "u":
    uv_index()