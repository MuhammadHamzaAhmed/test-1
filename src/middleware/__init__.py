import traceback

import jwt
from colorama import Fore, Style
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse

from src import app
from src.server.config import config


def print_exec_info(exc):
    print(Fore.MAGENTA + "==================================Error==================================")
    print(Fore.RED + f"Error occurred: {exc}")
    print(Fore.RED + traceback.format_exc())


@app.middleware("http")
async def error_handling_middleware(request: Request, call_next):
    try:
        print(Fore.MAGENTA + "\n\n==================================Request Started==================================")
        print(Fore.MAGENTA + "Client: ", Fore.YELLOW, request.client)
        print(Fore.MAGENTA + "Request: ", Fore.YELLOW, request.url)
        print(Fore.MAGENTA + "Method: ", Fore.YELLOW, request.method)
        print(Style.RESET_ALL)
        response = await call_next(request)
        return response
    except Exception as exc:
        print_exec_info(exc)
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            content="An internal server error occurred.")
    finally:
        print(Fore.MAGENTA + "==================================Request Ended==================================")
        print(Style.RESET_ALL)


async def authenticate_jwt(request: Request, level: str, signing_secret: str):
    authorization: str = request.headers.get('Authorization')
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token missing")

    scheme, _, token = authorization.partition(' ')
    if scheme.lower() != 'bearer':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization header invalid")
    try:
        decoded_token = jwt.decode(token, signing_secret, algorithms=["HS256"])
        if decoded_token.get('user') is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
        decoded_token = decoded_token.get('user')
        if decoded_token.get('level') is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User level not present")
        if decoded_token.get('level') != "superadmin":
            if decoded_token.get('roles') is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Roles not present")
            if decoded_token.get('level') != level:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User level not allowed")
            if "*" not in decoded_token.get('roles') and "heatmaps" not in decoded_token.get('roles'):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User role not allowed")
    except jwt.ExpiredSignatureError as exc:
        print_exec_info(exc)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
    except jwt.InvalidTokenError as exc:
        print_exec_info(exc)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalid")
    except jwt.InvalidSignatureError as exc:
        print_exec_info(exc)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token signature invalid")
    except HTTPException as exc:
        print_exec_info(exc)
        raise exc
    except Exception as exc:
        print_exec_info(exc)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")


async def admin_middleware(request: Request):
    await authenticate_jwt(request, "superadmin", config.get('TOKEN_SECRET_ADMIN'))


# User Middleware
async def user_middleware(request: Request):
    await authenticate_jwt(request, "user", config.get("TOKEN_SECRET"))
