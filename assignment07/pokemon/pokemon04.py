import aiofiles
import asyncio
import json
import os

pokemonapi_directory = "./assignment07/pokemon/pokemonapi"
pokemonmove_directory = "./assignment07/pokemon/pokemonmove"

async def main():
    pokemon_name = getPokemon()
    # Read the contents of the json file
    for pokeName in pokemon_name: 
        async with aiofiles.open(f"{pokemonapi_directory}/{pokeName}", mode='r') as f:
            contents = await f.read()

        # Load it into a dictionary and create a list of moves.
        pokemon = json.loads(contents)
        name = pokemon["name"]
        moves = [move["move"]["name"] for move in pokemon["moves"]]
        
        # Open a new file to write the list of moves into.
        async with aiofiles.open(f"{pokemonmove_directory}/{name}_moves.txt", mode='w') as f:
            await f.write("\n".join(moves))

def getPokemon():
    name = []
    for file in os.listdir("./assignment07/pokemon/pokemonapi/"):
        if file.endswith(".json"):
            name.append(file)

    return name
asyncio.run(main())




