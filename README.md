# TourOfHeroes

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 14.2.6 following Angular [TourOfHeroes Tutorial](https://angular.io/tutorial). After finishing the tutorial, [python 3.8.10](https://www.python.org/downloads/release/python-3810/) with [FastAPI](https://fastapi.tiangolo.com/) and [SQLAlchemy](https://www.sqlalchemy.org/) libraries and [PostgreSQL](https://www.postgresql.org/) for the database where used in the backend to complement the project.

## Development server

Run `ng serve` on the project folder for a dev server of the Angular app. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

Run `create_python_venv` on `./src/toh_api` in order to create a virtual python environment for TourOfHeroes API to run - for this step you should have Python's [venv](https://docs.python.org/3/library/venv.html) library intalled. Once the virtual environment is running, use `pip install -r requirements.txt` to install all of the API dependencies. After all is done, run `uvicorn main:app --reload` on the same folder for a dev server of the TourOfHeroes API, which will automatically reload after any changes on the source files the same way the Angular app will.

Last step is to run the PostgreSQL server, which one can achieve through Postgre's GUI interface [pgAdmin](https://www.pgadmin.org/). When your Postgre server is properly set, you should create file `db_config.py` in the folder `database` inside of the API's directory. Inside the file, add the following:

```Python
settings = {
    'user'   : 'DATABASE_USER',
    'pass'   : 'DB_USER_PASSWORD',
    'host'   : 'DATABASE_HOST', # which can be localhost or any other
    'port'   : '5432', # Database port is usually 5432 for Postgre
    'db_name': 'DATABASE_NAME',
    'db_type': 'postgresql' # or another, if you'd like
}
```

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.
