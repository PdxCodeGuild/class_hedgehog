"""
Mini Capstone: Python
April
June 2022
"""

import requests


def find_breweries():
    while True:
        menu = """
        Find Breweries, Breweries, Cideries 
        and Craft Beer Bottle Shops nearby

        1) Find location automatically
        2) Enter Zip Code
        3) Exit
        """
                
        choice = input(menu + "-> ")
        if choice == "1":
            ip_address = requests.get('https://api.ipify.org').text
            # print("IP address: {}".format(ip_address))

            #use IP adress and API to get location data
            loc_data = requests.get(f'https://ipapi.co/{ip_address}/json/')
            loc_data = loc_data.json()
            # print (loc_data)

            location_detail = {
            "IP": ip_address,
            "city": loc_data.get("city")
            }

            city = location_detail["city"]
            
            # use API to get up to 5 Breweries, Cideries and Craft Beer Bottle Shops nearby based on zip code
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
                phone_num = i["phone"] # format phone number later
                website = i["website_url"]
                print(f"\nName:\n{name}\nType:\n{type}\nAddress:\n{street}\n{city_b}, {state_b}\nPhone Number:\n{phone_num}\nWebsite:\n{website}\n")

            break

        elif choice == "2":
            zipcode2 = input("Enter Zipcode: ")
            responseb = requests.get(f"https://api.openbrewerydb.org/breweries?by_postal={zipcode2}&per_page=5")
            breweriesb = responseb.json()
            if len(breweriesb) <= 0:
                print("None Found")
            for i in breweriesb:
                name = i["name"]
                type = i["brewery_type"].title()
                street = i["street"]
                city_b = i["city"]
                state_b = i["state"]
                phone_num = i["phone"] ############### format phone number later
                website = i["website_url"]
                print(f"\nName:\n{name}\nType:\n{type}\nAddress:\n{street}\n{city_b}, {state_b}\nPhone Number:\n{phone_num}\nWebsite:\n{website}\n")

            break
            ########### figure out error message if incorrect user input/not a zip code

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Error")
            try_again = input("Try again?\n(y/n): ").lower()
        
        ############### put a try again option after done search not just after error
        
        if try_again.lower() != "y":
            print("Goodbye!")
            break

find_breweries()

