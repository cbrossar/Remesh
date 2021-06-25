# Remesh

## Setup local environment

1. Clone Repository
2. `cd Remesh`

### Run Backend

1. Install Python 3.8^
2. `cd remesh-api`
3. Create python virtual environment: `python3 -m venv venv`
4. Activate venv: `source venv/bin/activate`
5. Install requirements: `pip install -r requirements.txt`
6. Make Migrations: `python manage.py makemigrations`
7. Migrate: `python manage.py migrate`
8. Run Server: `python manage.py runserver`
   

### Run Frontend
1. Install Angular