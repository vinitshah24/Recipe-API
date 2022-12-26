# Recipe Rest API Django App

### :star: Backend: Python Django
Create virtual environment for the application:<br />
```
virtualenv app
```

Source scripts to activate the virtualenv:<br />
```
source Scripts/activate
```

Install requirements for the project:<br />
```
pip install -r requirements.txt
```

Create new project
```
django-admin startproject app .
```

Run ther server
```
python manage.py runserver
```

Create the app component
```
python manage.py startapp core
```

Make Migrations
```
python manage.py makemigrations
python manage.py migrate
```

python manage.py wait_for_db && \
python manage.py migrate && \
python manage.py runserver

Create superuser
```
python manage.py createsuperuser
```
