from pydantic import BaseModel


class PokemonInterface(BaseModel):
    name: str
    primary_type: str
    secondary_type: str = None
    level: int
    health_points: float

    class Config:
        from_attributes = True
