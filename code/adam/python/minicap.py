
import requests
from requests import get



#ip = input("Enter the IP address you would like to receive locational data for: ")
def grab_ip():
    ip = get('https://ipapi.co/ip/').text
    return ip

def main(ip=grab_ip()):
    """This goal of the function is to return data about the IP that the user inputs or that is retrieved from user.
        and store it in default file "visitors_ip.txt"
        default IP address is 8.8.8.8 (Google LLC.)
        """
#ip = "8.8.8.8"
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

    
#print(user_info)    
    
# lat = data["latitude"]
# long = data["longitude"]
#     #print(get('https://ipapi.co/ip/')).text
# print(lat,long)
#main()
    
    




#print(lat, long)