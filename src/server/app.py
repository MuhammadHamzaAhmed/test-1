import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from src.server.config import PORT, config
from src.server.mongo import CONNECTION_STRING

print(CONNECTION_STRING)

app: FastAPI = FastAPI(
    middleware=[
        Middleware(
            TrustedHostMiddleware,
            allowed_hosts=['*']
        ),
        Middleware(
            GZipMiddleware,
            minimum_size=1000
        )
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if os.getenv('NODE_ENV') == 'production':
    app.add_middleware(SentryAsgiMiddleware)

env = os.getenv('NODE_ENV')
if os.getenv('NODE_ENV') == 'secure':
    server = f"{'https://'}{config.get('NODE_HOST')}:{PORT}"
else:
    server = f"{'http://'}{config.get('NODE_HOST')}:{PORT}"
