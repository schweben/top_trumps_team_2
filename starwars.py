# This is a file that contains all the Star Wars specific functions
import requests
from pprint import pprint

"""
Star Wars API
● Homepage ★ https://swapi.dev/api/
● Documentation ★ https://swapi.dev/documentation
Learn about the People, Films, Species, Starships, Vehicles and Planets from Star Wars
'films': 'https://swapi.dev/api/films/'
'people': 'https://swapi.dev/api/people/'
'planets': 'https://swapi.dev/api/planets/'
'species': 'https://swapi.dev/api/species/'
'starships': 'https://swapi.dev/api/starships/'
'vehicles': 'https://swapi.dev/api/vehicles/'
"""

# Create a function which gets a dictionary for the character id given
# We should be able to get the data, like this example:
#     "name": "Luke Skywalker",
#     "height": "172",
#     "mass": "77",
#     "hair_color": "blond",
#     "skin_color": "fair",
#     "eye_color": "blue",
#     "birth_year": "19BBY", # Before the Battle of Yavin (end of first film) or After BY
#     "gender": "male",
#     "homeworld" - would need to interrogate the planets API
#     "species"- would need to interrogate the species API
#     "films"[] - don't need to ask which ones, just get the length - the more films they have been in, they win the round


def get_character_stats(character_number):
    # Set the path to our Star wars API (Application Programming Interface) which will respond to our information requests
    url = 'http://swapi.dev/api/people/{}'.format(character_number) # Unfortunately swapi.co is not maintained anymore

    # The requests library that we have imported can 'get' (pull down) information from the internet
    response = requests.get(url) # Check if you have a valid response from the internet
    if(response.status_code != 200):
        print("Error: Response Code {}, ID number: {}".format(response.status_code, character_number)) # e.g. 200 is okay, 404 is resource not found

    # Get the data from the response
    my_character = response.json() # JSON is used to format the data over the internet

    # Debug help
    #print(pprint(my_character))
    #print(my_character['name'])

    # Create a dictionary of name, id, height & weight;
    character_card = {
        "name": my_character['name'],
        "id": character_number,
        "height": my_character['height'],
        "weight": my_character['mass'],
        "films": len(my_character['films'])
    }
    # Help with the maths for comparisions
    # Contents must be numbers
    if character_card["height"] == "unknown":
        character_card["height"] = -1
    else:
        character_card["height"] = float(character_card["height"]) # float rather than int, as some characters in the database have a string containing a decimal point

    if character_card["weight"] == "unknown":
        character_card["weight"] = -1
    else:
        character_card["weight"] = float(character_card["weight"])

    return(character_card)