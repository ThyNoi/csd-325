# Eric Sengvanhpheng
# July 18, 2026
# Advanced Python 9.2

# Install requests library, use an API to retrieve data, and format the response.

import requests 
import json

# Send a request to Open Notify API to retrieve the current astronauts.
response = requests.get("http://api.open-notify.org/astros.json")

# Display the status code.
print(response.status_code)
print()

# Creates a function that takes a parameter, formats the text by json.dumps and prints it.
def jprint(obj): # Obj just a placeholder name to fill in later.
    text =json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

