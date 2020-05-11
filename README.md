# Online Bookstore

## Setup
1. Install virtualenv to create isolated Python environment. `pip install virtualenv`.
2. Create virtual environment in project folder. E.g. `virtualenv venv`

3. Activate virtual environment. \
Linux: `source venv/bin/activate`  
Windows: `venv\scripts\activate`

4. Install required packages. 
`pip install -r requirements.txt`

5. To populate data
`python manage.py loaddata db.json`

6. To run
`python manage.py runserver`