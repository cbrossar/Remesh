# Remesh

## Setup local environment

1. [Clone Repository](https://github.com/cbrossar/Remesh)

### Run Backend

1. Install Python 3.8^
2. `cd Remesh/remesh-api`
3. Create python virtual environment: `python3 -m venv venv`
4. Activate venv: `source venv/bin/activate`
5. Install requirements: `pip install -r requirements.txt`
6. Make Migrations: `python manage.py makemigrations`
7. Migrate: `python manage.py migrate`
8. Run backend: `python manage.py runserver`
   

### Run Frontend
1. [Install Node](https://nodejs.org/en/)
2. Install Angular CLI `npm install -g @angular/cli` [help](https://medium.com/@angela.amarapala/ways-to-fix-bash-ng-command-not-found-7f329745795)
3. `cd Remesh/remesh-gui`
4. Install packages: `npm i`
5. Run frontend: `ng serve`


### Run Tests
1. `cd Remesh/remesh-api`
2. Run unit tests: `python manage.py test crud.tests`
3. Run integration tests: 
    - `python manage.py test crud.tester.test_conversations`
    - `python manage.py test crud.tester.test_messages`
    - `python manage.py test crud.tester.test_thoughts`


### Design Decisions
- I decided that the Search Messages functionality should search within a conversation
- I decided to ignore the time inputs through the GUI. I thought it was unnecessary. 
As seen in the backend tests, you can still create objects with custom create datetimes
