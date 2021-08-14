#!/usr/bin/env python3

import csv
import secrets

national_pokedex = []
national_pokedex_url = "https://pokemondb.net/pokedex/"

with open('pokemon.csv', 'r', encoding='utf-8') as csv_file:

    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        pokemon_entry = f"{line['NUMBER']} | {line['NAME']} | {national_pokedex_url+line['NUMBER']} | {line['TYPE1']}"

        if line['TYPE2']:
            pokemon_entry += f"-{line['TYPE2']}"

        national_pokedex.append(pokemon_entry)

print("Who's that Pokemon!?")
print(secrets.choice(national_pokedex))

# TODO: create a second array that holds helps avoid repetition
