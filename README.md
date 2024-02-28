Weather API 

This application has a dependency on SQL Lite.
To set this application in your local machine, follow the instructures

1. Create a new virtual environment
```
python3 -m venv venv
```
2. Activate virtual environment
```
source venv/bin/activate
```
3. Pip install all the requirements
```
pip install -r requirements.txt
```
4. Run the application
```
FLASK_RUN_PORT=5900 flask run
```
5. Invoke `http://127.0.0.1:5900/` on chrome to verify the launch. 
