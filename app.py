import errno

import uvicorn
from colorama import Fore, Style

from src import server
from src.server.app import env
from src.server.config import PORT, PROJECT_NAME

if __name__ == "__main__":
    try:
        print(f"{PROJECT_NAME} running on http://localhost:{PORT}")
        print('--')
        print(Fore.YELLOW + f"Environment:     {env}")
        print(Fore.MAGENTA + f"Server:     {server}")
        print("--")
        print(Style.RESET_ALL)
        uvicorn.run("src:app", port=PORT, host='0.0.0.0', reload=True)
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            print(Fore.RED + f"Port {PORT} is already in use.")
        else:
            raise
    except Exception as e:
        print(Style.RESET_ALL)
        print(f"An unexpected exception occurred: {e}")
