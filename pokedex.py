import requests

def search_pokemon(*name):
    for i, item in enumerate(list(name)):
        convert = str.lower(item)
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{convert}/")
        pokemon = response.json()
        if i == 0:
            print("This is your 1st pokemon")
        elif i == 1:
            print("This is your 2nd pokemon")
        elif i == 2:
            print("This is your 3rd pokemon")
        else:
            print("This is your {}th pokemon".format(i+1))
        print("Name: " + str.title(pokemon["name"]))
        print("ID: " + str(pokemon["id"]))
        print("Base XP: " + str(pokemon["base_experience"]))
        print("---------")

if __name__ == "__main__":
    pokemon1= input("List your 1st pokemon in the party: ")
    pokemon2= input("List your 2nd pokemon in the party: ")
    pokemon3= input("List your 3rd pokemon in the party: ")
    pokemon4= input("List your 4th pokemon in the party: ")
    pokemon5= input("List your 5th pokemon in the party: ")
    pokemon6= input("List your 6th pokemon in the party: ")
    search_pokemon(pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6)