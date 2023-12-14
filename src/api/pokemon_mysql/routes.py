from typing import List

from src.api.pokemon_mysql.controller import (delete_pokemon, get_pokemon,
                                              post_pokemon, post_pokemon_list,
                                              put_pokemon)
from src.api.pokemon_mysql.interfaces import PokemonInterface
from src.server.routes import user_router

user_router.add_api_route("/pokemon", get_pokemon, methods=["GET"], response_model=List[PokemonInterface])
user_router.add_api_route("/pokemon", post_pokemon, methods=["POST"], response_model=str)
user_router.add_api_route("/pokemon/file", post_pokemon_list, methods=["POST"], response_model=str)
user_router.add_api_route("/pokemon/{id_}", put_pokemon, methods=["PUT"], response_model=str)
user_router.add_api_route("/pokemon/{id_}", delete_pokemon, methods=["DELETE"], response_model=str)
