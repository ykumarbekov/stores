Django RESTFull API application "Local Store"  
----
Contains pluggable applications 
Instructions for deployment  
1) Clone the project, open it inside Pycharm IDE  
2) Initialize Virtualenv (Preferences - Project interpreter - Add), use Python version 3.6 and above  
3) Open venv terminal and install libraries:   
- Django framework: pip install django  
- PostgreSQL driver: pip install psycopg2-binary  
- Django REST API: pip install djangorestframework  
  Pay attention: Before start working - You should generate SECRET_KEY and export it  
  Use this link for generating: https://djecrety.ir/  
  Create folder keys and save generated key, create file for this purpose as example: ./keys/keys.txt  
  ```
  export SECRET_KEY = 'xxxx'  
  cd localstores 
  python manage.py startap application
  ```
4) Set up Database settings, file: settings.py  