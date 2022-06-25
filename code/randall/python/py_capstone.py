# Python ₘᵢₙᵢ capstone
# UV index and Weather API
# Weather  ---  https://openweathermap.org/api
# UV Index ---  https://data.epa.gov/efservice/getEnvirofactsUVDAILY/ZIP

from colorama import Fore  # for purdy colors
import requests
import creds     #import external file (creds.py added to .gitignore) which contains
                 # the API key with the variable "api_key". Keeps API key secret

def weather():      # Not getting accurate weather data ///fixed by removing USA from the url
    """This function will return the general weather conditions of the entered city"""

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    city = input(Fore.GREEN +"For current weather conditions, please enter a city name: ")
    state = input(Fore.GREEN +"Please enter the state: ")
    requests_url = f"{base_url}?q={city},{state},&appid={creds.api_key}"
    response = requests.get(requests_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"]
        print(Fore.YELLOW + weather[0]["description"].title())
        temperature = round(data["main"]["temp"] - 273.15) * 9/5 + 32 #Converts Kelvin to Fahrenheit and rounds 
        print(Fore.YELLOW + f"Temperature: {temperature} °f")
    else:
        print("Error")

def uv_index():
    """This function will return the UV index of the entered zip code"""

    zip_code = input(Fore.WHITE +"Please enter the Zip Code: ") 
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
           print(Fore.GREEN + "UV Index 0-2 means minimal danger from the sun’s UV rays for the average person. Most people can stay in the sun for up to one hour during peak sun (10 am to 4 pm) without burning. However, people with very sensitive skin and infants should always be protected from prolonged sun exposure.")
        elif uv <= 5:
              print(Fore.YELLOW + "UV Index 3-5 means low risk of harm from unprotected sun exposure. Fair-skinned people, however, may burn in less than 20 minutes. Wearing a hat with a wide brim and sunglasses will protect your eyes. Always use a broad-spectrum sunscreen with an SPF of at least 30, and wear long-sleeved shirts when outdoors.")
        elif uv <= 7:                                                           
                print(Fore.YELLOW + "UV Index 6-7 means moderate risk of harm from unprotected sun exposure. Fair-skinned people, however, may burn in less than 20 minutes. Wearing a hat with a wide brim and sunglasses will protect your eyes. Always use a broad-spectrum sunscreen with an SPF of at least 30 and wear long-sleeved shirts when outdoors. Remember to protect sensitive areas like the nose and the rims of the ears. Sunscreen prevents sunburn and some of the sun’s damaging effects on the immune system. Use a lip balm or lip cream containing a sunscreen.")
        elif uv <= 10:
                print(Fore.RED + "UV Index 8-10 means high risk of harm from unprotected sun exposure. Fair-skinned people may burn in less than 10 minutes. Minimize sun exposure during midday hours of 10 am to 4 pm. Protect yourself by liberally applying a broad-spectrum sunscreen of at least SPF 30. Wear protective clothing and sunglasses to protect the eyes. When outside, seek shade. Don’t forget that water, sand, pavement, and glass reflect UV rays even under a tree, near a building or beneath a shady umbrella. Wear long-sleeved shirts and trousers made from tightly-woven fabrics. UV rays can pass through the holes and spaces of loosely knit fabrics.")
        elif uv >= 11:
                print(Fore.RED + "UV Index of 11+ means a very high risk of harm from unprotected sun exposure. Fair skinned people may burn in less than 5 minutes. Outdoor workers and vacationers who can receive very intense sun exposure are especially at risk. Minimize sun exposure during midday hours of 10 am to 4 pm. Apply broad-spectrum SPF 30+ sunscreen every 2 hours, more frequently if you are sweating or swimming. Avoid being in the sun as much as possible and wear sunglasses that block out 99-100% of all UV rays (UVA and UVB). Wear a hat with a wide brim which will block roughly 50% of UV radiation from reaching the eyes.")
    else:
        print("Error")

user_input = input(Fore.GREEN + "###  Welcome to Weather & UV Index Checker  ###\n Type (w) for Weather or (u) for UV index:  ").lower()

if user_input == "w":
    weather()
elif user_input == "u":
    uv_index()