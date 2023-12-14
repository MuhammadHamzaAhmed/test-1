from typing import List

from fastapi import HTTPException

from src.api.pokemon_mongo.interfaces import PokemonInterface
from src.api.pokemon_mongo.models import Pokemons


async def get_pokemon() -> List[PokemonInterface]:
    pokemons = Pokemons.objects()
    return [PokemonInterface(**pokemon.dict()) for pokemon in pokemons]


async def post_pokemon(pokemon: PokemonInterface) -> str:
    pokemon = Pokemons(**pokemon.model_dump())
    pokemon.save()
    return "Pokemon added successfully"


async def put_pokemon(id_: str, pokemon_interface: PokemonInterface) -> str:
    pokemon: Pokemons = Pokemons.objects(id=id_).first()
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")

    pokemon.name = pokemon_interface.name
    pokemon.primary_type = pokemon_interface.primary_type
    pokemon.level = pokemon_interface.level
    pokemon.health_points = pokemon_interface.health_points
    pokemon.attack_point = pokemon_interface.attack_point

    pokemon.update(
        set__name=pokemon.name,
        set__primary_type=pokemon.primary_type,
        set__level=pokemon.level,
        set__health_points=pokemon.health_points,
        set__attack_point=pokemon.attack_point
    )

    return "Pokemon updated successfully"


async def delete_pokemon(id_: str) -> str:
    pokemon: Pokemons = Pokemons.objects(id=id_).first()
    if not pokemon:
        raise HTTPException(status_code=504, detail="Pokemon not found")
    pokemon.delete()
    return "Pokemon deleted successfully"
