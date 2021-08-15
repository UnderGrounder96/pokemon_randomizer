#!/usr/bin/env python3

import os
import sys
import csv
import secrets
import webbrowser

pokemon_entry = ''
national_pokedex = []


def preflight_check():
    """This function creates our pokemon 'database' if it doesn't exist"""

    if os.path.exists("pokemon.csv"):
        return

    import requests

    pokemon_csv_url = "https://gist.githubusercontent.com/simsketch/1a029a8d7fca1e4c142cbfd043a68f19/raw/bd584ee6c307cc9fab5ba38916e98a85de9c2ba7/pokemon.csv"
    requests_get = requests.get(pokemon_csv_url)

    with open("pokemon.csv", "wb") as pokemon_csv_file:
        pokemon_csv_file.write(requests_get.content)


def create_pokedex():
    """This function creates entry in our national pokedex from 'database'"""

    pokedex_url = "https://pokemondb.net/pokedex/"

    with open("pokemon.csv", "r", encoding="utf-8") as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            pokemon_entry = f"{line['NUMBER']} | {line['NAME']} | {pokedex_url+line['NUMBER']} | {line['TYPE1']}"

            if line['TYPE2']:
                pokemon_entry += f"-{line['TYPE2']}"

            national_pokedex.append(pokemon_entry)


def select_pokemon():
    """This function selects the pokemon and removes the pokemon from 'database'"""

    global pokemon_entry

    try:
        pokemon_entry = secrets.choice(national_pokedex)
    except IndexError as e:
        print(f"IndexError: {e.__str__()}")
        print("Removing the pokemon.csv database, please re-run the program!")
        os.remove("pokemon.csv")
        sys.exit(0)

    with open("pokemon.csv", "r+", encoding="utf-8") as pokemon_csv:
            pokemon_selected = pokemon_entry.split(' | ')[1]

            pokemon_file = pokemon_csv.readlines()

            pokemon_csv.seek(0) # Change the file position

            for line in pokemon_file:

                if pokemon_selected not in line:
                    pokemon_csv.write(line)

            pokemon_csv.truncate() # Resizes the file to a specified size

    print("Who's that Pokemon!?")
    print(pokemon_entry)

    webbrowser.open_new_tab(pokemon_entry.split(' | ')[2])


def main():

    preflight_check()

    create_pokedex()

    select_pokemon()


    sys.exit(0)



if __name__== "__main__":
    main()
