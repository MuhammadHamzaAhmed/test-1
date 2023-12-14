from uuid import uuid4

from mongoengine import Document, IntField, StringField


class Pokemons(Document):
    id = StringField(required=True, primary_key=True, default=lambda: str(uuid4()))
    name = StringField(required=True)
    primary_type = StringField(required=True)
    level = IntField(required=True)
    health_points = IntField(required=True)
    attack_point = IntField(required=True)
    meta = {'collection': 'pokemons'}

    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "primary_type": self.primary_type,
            "level": self.level,
            "health_points": self.health_points,
            "attack_point": self.attack_point
        }
