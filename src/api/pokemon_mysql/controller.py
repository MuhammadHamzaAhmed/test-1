from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.pokemon_mysql.interfaces import PokemonInterface
from src.api.pokemon_mysql.middleware import get_pokemon_list_from_file
from src.api.pokemon_mysql.models import Pokemon
from src.server.mysql import get_db


async def get_pokemon(db: Session = Depends(get_db)) -> List[PokemonInterface]:
    pokemons = db.query(Pokemon).all()
    return [PokemonInterface.model_validate(pokemon) for pokemon in pokemons]


async def post_pokemon(pokemon: PokemonInterface, db: Session = Depends(get_db)) -> str:
    pokemon = Pokemon(**pokemon.model_dump())
    db.add(pokemon)
    db.commit()
    return "Pokemon added successfully"


async def post_pokemon_list(pokemon_list: List[PokemonInterface] = Depends(get_pokemon_list_from_file),
                            db: Session = Depends(get_db)) -> str:
    for pokemon in pokemon_list:
        pokemon = Pokemon(**pokemon.model_dump())
        db.add(pokemon)
    db.commit()
    return "Pokemon added successfully"


async def put_pokemon(id_: int, pokemon_interface: PokemonInterface, db: Session = Depends(get_db)) -> str:
    pokemon = db.query(Pokemon).filter_by(id=id_).first()
    if not pokemon:
        raise HTTPException(status_code=504, detail="Pokemon not found")
    pokemon.name = pokemon_interface.name
    pokemon.primary_type = pokemon_interface.primary_type
    pokemon.secondary_type = pokemon_interface.secondary_type
    pokemon.level = pokemon_interface.level
    pokemon.health_points = pokemon_interface.health_points
    db.commit()
    return "Pokemon updated successfully"


async def delete_pokemon(id_: int, db: Session = Depends(get_db)) -> str:
    pokemon = db.query(Pokemon).filter_by(id=id_).first()
    if not pokemon:
        raise HTTPException(status_code=504, detail="Pokemon not found")
    db.delete(pokemon)
    db.commit()
    return "Pokemon deleted successfully"
