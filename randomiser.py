#!/usr/bin/env python3

import csv
import secrets
import webbrowser

from os import path

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

pokemon_entry = secrets.choice(national_pokedex)

if path.exists("pokemon.log"):
    with open('pokemon.log', 'r', encoding='utf-8') as log_file:
        # TODO: create a fix for all pokemon exhaustion
        while pokemon_entry in log_file.read():
            pokemon_entry = secrets.choice(national_pokedex)

with open('pokemon.log', 'a' ) as log_file:
    log_file.write(pokemon_entry+'\n')

print("Who's that Pokemon!?")
print(pokemon_entry)

webbrowser.open_new_tab(pokemon_entry.split(' | ')[2])
