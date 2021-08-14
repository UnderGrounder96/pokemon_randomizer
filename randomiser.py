#!/usr/bin/env python3

import csv
import secrets
import webbrowser

pokemon_entry = ''
national_pokedex = []
national_pokedex_url = "https://pokemondb.net/pokedex/"

with open('pokemon.csv', 'r', encoding='utf-8') as csv_file:

    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        pokemon_entry = f"{line['NUMBER']} | {line['NAME']} | {national_pokedex_url+line['NUMBER']} | {line['TYPE1']}"

        if line['TYPE2']:
            pokemon_entry += f"-{line['TYPE2']}"

        national_pokedex.append(pokemon_entry)

# TODO: create a second array that helps avoiding repetition
print("Who's that Pokemon!?")

pokemon_entry = secrets.choice(national_pokedex)

webbrowser.open_new_tab(pokemon_entry.split(' | ')[2])

print(pokemon_entry)
