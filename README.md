# Project Description :

# How to use it : 

#### Dashboard
```bash
$ cd Dashboard
$ pip3 install -r requirements.txt
$ python run.py
```
```bash
< PROJECT ROOT >
   |
   |-- app/                      # Implements app logic
   |    |-- base/                # Base Blueprint - handles the authentication
   |    |-- home/                # Home Blueprint - serve UI Kit pages
   |    |
   |   __init__.py               # Initialize the app
   |
   |-- requirements.txt          # Development modules - SQLite storage
   |-- requirements-mysql.txt    # Production modules  - Mysql DMBS
   |-- requirements-pqsql.txt    # Production modules  - PostgreSql DMBS
   |
   |-- .env                      # Inject Configuration via Environment
   |-- config.py                 # Set up the app
   |-- run.py                    # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```
#### API
```bash
$ cd API_prediction
$ pip3 install -r requirements.txt
$ python app.py
```
```bash
< PROJECT ROOT >
   |
   |-- api/                      # Implements app logic
   |    |-- Ressources/             # Base Blueprint - handles the authentication
   |      | -- endpoints
   |        | -- prediction.py  
   |      | -- operations
   |      | -- serializers
   |      | -- __init__py
   |    |-- restplus.py             # 
   |    |-- __init__.py
   |   __init__.py               # Initialize the app
   |
   |-- settings.py               # Set up the app
   |-- app.py                    # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```
> Note: To use the app, please run the Dashboard and API.

