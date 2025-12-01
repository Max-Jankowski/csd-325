# Max Jankowski
# CSD-325 module 9 assignment
# Bellevue University

# I was originally working on a futurama api, but after several hours I was getting error 500 server issues
# I switched to the dragon ball api and found that it had a lot of clear documentation and the site was easy on the eyes.


import requests #importing libraries
import json

print("=" * 60)  #formating the header
print("DRAGON BALL API DEMONSTRATION")
print("=" * 60)
print()

print("Step 1: Testing connection to Dragon Ball API...") # step 1 of this process, testing the connection
print("-" * 60)

api_url = "https://dragonball-api.com/api/characters?limit=10"
response = requests.get(api_url) #defining the api endpoint and making a request, process found in module tutorial

print("URL:", api_url) #display info on connection
print("Status Code:", response.status_code) # a 200 is success as per module reading

if response.status_code == 200: #verifing successful connection
    print("✓ Connection successful!")
else:
    print("✗ Connection failed!")
    exit() # exit clause is connection failed

print() # formating for separation of lines

print("Step 2: Raw JSON Response (first 500 characters)...")
print("-" * 60) #step 2, displaying the raw json response

raw_text = response.text # getting text response from api

print(raw_text[:500] + "...") # printing the first 500 characers
print()

print("Step 3: Formatted Response - Dragon Ball Characters")
print("-" * 60)

data = response.json() # json response into py dictionary, instruction from module reading

print("Total characters retrieved:", len(data['items'])) # displaying total characters received
print()

print("Dragon Ball Z Characters:") #header for character info
print()

for i, character in enumerate(data['items'], 1): #iteration for characters

    print("{}. {}".format(i, character['name'])) # displaying a character name
    # using the .get() method to access keys that may exist, returns unkown if missing
    print("   Race: {}".format(character.get('race', 'Unknown')))
    print("   Gender: {}".format(character.get('gender', 'Unknown')))
    print("   Ki: {}".format(character.get('ki', 'Unknown')))
    print("   Max Ki: {}".format(character.get('maxKi', 'Unknown')))
    print("   Affiliation: {}".format(character.get('affiliation', 'Unknown')))
    print() # This formating was determined by looking at what information was available from the APi as per the documentation

print("=" * 60) # getting detailed info about everyone fav. character in the show
print("Getting detailed info for Goku...")
print("=" * 60)
print()

goku_url = "https://dragonball-api.com/api/characters/1" # making api request for his info

goku_response = requests.get(goku_url)
goku_data = goku_response.json() #parsing the info for his data

# displaying details
print("Name:", goku_data['name'])
print("Race:", goku_data['race'])
print("Ki:", goku_data['ki'])
print("Max Ki:", goku_data['maxKi'])
print("Description:", goku_data['description'][:200] + "...")
print()

# Checking if these 'tranformations' exist and displaying if they do
if 'transformations' in goku_data and goku_data['transformations']:
    print("Transformations:")
    for transform in goku_data['transformations']:
        print("  -", transform['name'])

# formatting the footer of the program. informing user the process is done
print()
print("=" * 60)
print("END OF DEMONSTRATION")
print("=" * 60)

# Resources
# https://web.dragonball-api.com/documentation for documentation on their api
# https://docs.python-requests.org/en/latest/ used multiple links to get answers about request after working through some errors
# https://realpython.com/python-json/ used to aid with some syntax issues I had
# https://www.w3schools.com/python/python_json.asp the w3 go to for reference