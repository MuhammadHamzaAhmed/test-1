from sqlalchemy import Column, Float, Integer, String

from src.server.mysql import Base


class Pokemon(Base):
    __tablename__ = 'pokemons'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    primary_type = Column(String)
    secondary_type = Column(String, nullable=True)
    level = Column(Integer)
    health_points = Column(Float)
