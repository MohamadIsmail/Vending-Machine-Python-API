# FlapKap-Task
This is an implemnentation for FlapKap backend task by Mohamed Ismail.
The task is written in python-flask using sqlite database(SQLAlchemy)
# How to run the API 
- run those commands on your linux machine to install python latest version and its dependencies:
   - `sudo apt update`
   - `sudo apt install python3.10`
   - `sudo apt install python3.10-venv`
   - `python3 -m venv env`
- run the application inside virtual environment by running this command:
   - `source env/bin/activate`
- install requirements inside virtual enviroment:
   - `pip3 install -r requirements.txt`
- initiate the database:
   - `flask db init`
   - `flask db migrate -m "Initial migration."`
   - `flask db upgrade`
- run the flask application
   - `flask run`
# How to run tests
- first, follow the application running commands above.
- second, run the test script:
   - `python3 test_app.py`
