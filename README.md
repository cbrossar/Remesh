# Remesh

## Setup local environment

1. Install Python 3.8^
2. Clone Repository
3. `cd Remesh`

### Run Backend

1. `cd remesh-api`
2. Create python virtual environment: `python3 -m venv venv`
3. Activate venv: `source venv/bin/activate`
4. Install requirements: `pip install -r requirements.txt`
5. Make Migrations: `python manage.py makemigrations`
6. Migrate: `python manage.py migrate`
7. Run Server: `python manage.py runserver`
    