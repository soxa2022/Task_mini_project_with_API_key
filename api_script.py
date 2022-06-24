import requests
import json
from colorama import Fore

print("The range of the input is from 1000 to 9974")
zip_code = int(input("Enter 4 digits (zip code): "))

# api key/request url
key = f'https://api.zippopotam.us/BG/{zip_code}'
# if you have problem with SSL certificate use this key:
# key = f'http://api.zippopotam.us/BG/{zip_code}'
# get requested data form url

data = requests.get(key)
data = data.json()
if len(data) == 0:
    print('\nWrong zip code')
    quit()

print(Fore.LIGHTBLUE_EX, f"\nCity name: {data['places'][0]['place name']}")
print(f"GPS coordinates: {float(data['places'][0]['latitude'])} , {float(data['places'][0]['longitude'])}")
print(f"State area: {data['places'][0]['state']}")
print(f"Abbreviation: {data['places'][0]['state abbreviation']}")
