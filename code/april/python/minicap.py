"""
Mini Capstone: Python
April
June 2022

Find Breweries, Brewpubs, Cideries and Craft Beer Bottle Shops near a given location
"""

import requests
import re


def find_breweries():
    while True:
        menu = """
        Find Breweries, Brewpubs, Cideries 
        and Craft Beer Bottle Shops nearby

        1) Find location automatically
        2) Enter Zip Code
        3) Done
        """
                
        choice = input(menu + "-> ")
        if choice == "1":
            ip_address = requests.get('https://api.ipify.org').text

            #use IP adress and API to get location data
            loc_data = requests.get(f'https://ipapi.co/{ip_address}/json/')
            loc_data = loc_data.json()

            location_detail = {
            "IP": ip_address,
            "city": loc_data.get("city")
            }

            city = location_detail["city"]
            
            # use location data and API to get up to 5(set 5 as a limit) Breweries, Cideries and 
            # Craft Beer Bottle Shops nearby based on zip code
            response = requests.get(f"https://api.openbrewerydb.org/breweries?by_city={city}&per_page=5")
            breweries = response.json()
            if len(breweries) <= 0:
                print("None Found")
            for i in breweries:
                name = i["name"]
                type = i["brewery_type"].title()
                street = i["street"]
                city_b = i["city"]
                state_b = i["state"]
                phone_num = i["phone"] 
                website = i["website_url"]
                print(f"\nName:\n{name}\nType:\n{type}\nAddress:\n{street}\n{city_b}, {state_b}\nPhone Number:\n{phone_num}\nWebsite:\n{website}\n")

            continue
        
        # allow user to enter a zipcode to find 
        elif choice == "2":
            zipcode2 = input("Enter Zipcode: ")

            regexp = re.compile("^\d{5}$")
            if not regexp.search(zipcode2):
                print(f"{zipcode2} is not a valid zipcode.\nPlease enter a valid zipcode.")
                continue

            responseb = requests.get(f"https://api.openbrewerydb.org/breweries?by_postal={zipcode2}&per_page=5")
            breweriesb = responseb.json()
            
            if len(breweriesb) <= 0:
                print("None found")
            for i in breweriesb:
                name = i["name"]
                type = i["brewery_type"].title()
                street = i["street"]
                city_b = i["city"]
                state_b = i["state"]
                phone_num = i["phone"] 
                website = i["website_url"]
                print(f"\nName:\n{name}\nType:\n{type}\nAddress:\n{street}\n{city_b}, {state_b}\nPhone Number:\n{phone_num}\nWebsite:\n{website}\n")

            continue

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Error")
            try_again = input("Try again?\n(y/n): ").lower()
    

        if try_again.lower() != "y":
            print("Goodbye!")
            break
        

find_breweries()
