from typing import List

from src.server.routes import admin_router
from src.api.pokemon_mongo.controller import (delete_pokemon, get_pokemon,
                                              post_pokemon, put_pokemon)
from src.api.pokemon_mongo.interfaces import PokemonInterface

admin_router.add_api_route("/pokemon", get_pokemon, methods=["GET"], response_model=List[PokemonInterface])
admin_router.add_api_route("/pokemon", post_pokemon, methods=["POST"], response_model=str)
admin_router.add_api_route("/pokemon/{id_}", put_pokemon, methods=["PUT"], response_model=str)
admin_router.add_api_route("/pokemon/{id_}", delete_pokemon, methods=["DELETE"], response_model=str)
