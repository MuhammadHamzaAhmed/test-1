# Fast API Template

## Table of Contents
- [Overview](#overview)
- [Installation Instructions](#installation-instructions)
- [Project Structure](#project-structure)
- [Usage Instructions](#usage-instructions)
- [API Documentation](#api-documentation)
- [Git Workflow](#git-workflow)
- [Contributing](#contributing)
- [License](#license)


## Overview
Fast API Template is designed to showcase the recommended structure for FastAPI projects. It features CRUD operations with MongoDB and MySQL databases, serving as a practical guide for developers.

## Installation Instructions
1. Create a directory and within it, create a `development.env` file.
2. Clone this repository next to the `development.env` file.
3. Navigate to the cloned project directory.
4. Create a virtual environment with `python -m venv venv` in linux and mac and `python -m virtualenv venv` for windows. In case of error run `pip install venv` in mac or linux or `pip install virtualenv` in windows. 
5. Activate the virtual environment with `source venv/bin/activate` in mac and linux. For windows, run `venv\Scripts\activate`.
6. Run `pip install -r requirements.txt` to install dependencies.
7. Navigate back to the parent directory. Obtain the `development.env` file from the project owner or copy from `./cloned_project/src/server/config.py`.
8. Set up the environment variable `NODE_ENV` to `development`.
9. Run `python app.py` to start the project.

## Project Structure
- `app.py`: Main file to start the project.
- `requirements.txt`: Project dependencies.
- `src`: Contains all the source code.
- `src/api`: Contains API modules.
  - `controller.py`: Business logic.
  - `interfaces.py`: API interfaces for request validation.
  - `middleware.py`: Middleware for data processing.
  - `models.py`: Database models.
  - `routes.py`: API routes.
- `src/libraries`: Reusable code (e.g., `reusable_code.py`).
- `src/middleware`: Project-wide middleware.
- `src/server`: Server-related code.
  - `config.py`: Project configuration.
  - `mongo.py`: MongoDB connection.
  - `mysql.py`: MySQL connection.
  - `routes.py`: Sub-routes for controllers.

## Usage Instructions
1. Use Postman to test the APIs.
2. Import module collections from the `json` folder of each module into Postman.
3. Follow module addition guidelines for integrating new modules and APIs.
4. Import new module routes in `src/server/imports.py` at the end of file.

## API Documentation
- Access the auto-generated FastAPI documentation at `http://{host}:{port}/docs`.

## Git Workflow
1. Create a branch from the master branch.
2. After completing tasks, create a pull request to the master branch.
3. Request a review from the project owner.
4. After merging, delete the branch.
5. Run `isort .` to ensure all imports are sorted.
6. Run `flake8 .` for linting checks before pushing code.

## Contributing
Follow the coding standards for naming conventions, ensuring no duplicate code, linting errors, or unused elements (variables, imports, functions, classes, modules, arguments, returns).

## License
© 2023, Signalytics AI. All Rights Reserved. This software is confidential and proprietary to Signalytics AI. Unauthorized use or distribution is strictly prohibited and may be subject to legal action.