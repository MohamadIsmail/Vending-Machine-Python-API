# FlapKap-Task
This is an implemnentation for FlapKap backend task by Mohamed Ismail.
The task is written in python-flask using sqlite database(SQLAlchemy)
# how to run it 
1.run those commands on your linux machine to install python latest version and its dependencies:
`sudo apt update`
`sudo apt install python3.10`
`sudo apt install python3.10-venv`
`python3 -m venv env`
2.run the application inside virtual envrionment by running this command:
`source env/bin/activate`
3. install requirements inside virtual enviroment:
`pip3 install -r requirements.txt`
4. initiate the database
`flask db init`
`flask db migrate -m "Initial migration."`
`flask db upgrade`
5. run the flask application
`flask run`