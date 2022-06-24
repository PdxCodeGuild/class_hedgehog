
import requests
from requests import get

def grab_ip():
    ip = get('https://ipapi.co/ip/').text
    return ip

def main(ip=grab_ip()):
    """The goal of this function is to return data about the IP that the user inputs or that is retrieved from user.
        and store it in a default file "visitors_ip.txt"
        
        This function requires one argument.
        ip: the default is to grab the ip from the computer running the function.
            but the user can input an ip in str form example("8.8.8.8").
        """

    response = get(f"https://ipapi.co/{ip}/json/")
    user_data = response.json()
   

    user_ip = user_data['ip']
    city = user_data['city']
    region = user_data['region']
    country = user_data['country']
    lat = user_data['latitude']
    long = user_data['longitude']
    file1 = open("visitors_ip.txt", "a")
    file1.write(f"""
    IP: {user_ip}, City: {city}, Region: {region}, Country: {country},
    Coordinate: Latitude {lat}, Longitude {long}""")

    file1.write("\n")
    file1.close()
    
    return(f"""
    IP: {user_ip}, City: {city}, Region: {region}, Country: {country},
        Coordinate: Latitude {lat}, Longitude {long}""")

print(main())
