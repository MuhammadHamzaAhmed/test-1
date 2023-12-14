from pydantic import BaseModel


class PokemonInterface(BaseModel):
    id: str = ""
    name: str
    primary_type: str
    level: int
    health_points: int
    attack_point: int

    class Config:
        from_attributes = True
