# Max Jankowski
# CSD-325 module 9 assignment
# Bellevue University

# used the reading/ tutorial material provided in this week's module
# getting simple info about whos in space

import requests
import json

# making a get request to open-notify api
response = requests.get("http://api.open-notify.org/astros.json")

# checking the status and code of response
print("Status Code:", response.status_code)
print() # separation for display formatting

data = response.json() # Parsing the JSOn response in the python library

print("Number of people in space:", data['number'])
print() #displaying the information about how many people are in space

print("Current astronauts in space:") # print information about what is going to display

# iterating through the list of astronauts in space
for person in data['people']: # I went with different formating then the reading, but I think it looks alot cleaner
    print("{} on the {}".format(person['name'], person['craft'])) # formating how info will be displayed