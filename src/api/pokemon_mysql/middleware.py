from fastapi import File, HTTPException, UploadFile

from .interfaces import PokemonInterface


def get_pokemon_list_from_file(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=500, detail="Invalid file format. Please upload a csv file.")

    contents = file.file.read().decode('utf-8')
    contents = contents.split('\n')
    pokemon_list = []
    for content in contents:
        content = content.split(',')
        pokemon_list.append(
            PokemonInterface(name=content[0], primary_type=content[1], secondary_type=content[2], level=int(content[3]),
                             health_points=float(content[4])))
    return pokemon_list
