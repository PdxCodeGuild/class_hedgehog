# Python ₘᵢₙᵢ capstone

# On this day in history API

import datetime
import requests

month = input("Welcome to the On this Day API!\n\nEnter a month (1 - 12): ")
day = input("Enter a day (1 - 31): ")
year = input("Enter a year: ")

url_events = 'https://byabbe.se/on-this-day/{}/{}/events.json'
url_people = 'https://byabbe.se/on-this-day/{}/{}/people.json'
url_deaths = 'https://byabbe.se/on-this-day/{}/{}/deaths.json'


"""
headers = {
  "wikipedia": "https://en.wikipedia.org/wiki/{}",
  "date": "https://byabbe.se/on-this-day/{}/{}",
}
"""

def get_category(url):
    response = requests.get(url)
    results = response.json()["results"]
    for result in results:
        print(result["title"])