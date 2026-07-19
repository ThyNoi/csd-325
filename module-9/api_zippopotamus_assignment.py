# Eric Sengvanhpheng
# July 18, 2026
# Advanced Python 9.2

# Create program to use simple api, retrieve data and format it
# This program uses Zippopotam.us API to retrieve location
# information for a U.S. zipcode and displays the JSON response.

import requests
import json

# Request location data for ZIP code 90210.
response = requests.get("https://api.zippopotam.us/us/90210")
print(response.status_code)
print()

# Print no formatting.
print(response.json())
print()

# Creates a function that takes a parameter, formats the text by json.dumps and prints it.
def jprint(obj): # obj just a placeholder name to fill in later.
    text =json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

