from src.server.app import app
from src.server.routes import base_route
from src.api.pokemon_mongo.routes import admin_router
from src.api.pokemon_mysql.routes import user_router


app.include_router(user_router)
app.include_router(base_route)
app.include_router(admin_router)
