# Todo List

### Steps

- Create virtual environment
  - `python3 -m virtualenv venv`
  - `py -m virtualenv venv`
- Activate virutal environment
  - `source venv/bin/activate`
  - `venv\Scripts\activate`
- Install django
  - `pip install django`
- Freeze requirements
  - `pip freeze > requirements.txt`
- Start new project
  - `django-admin startproject {project-name} .`
- Start new app
  - `python manage.py startapp {appname}`
  - `py manage.py startapp {appname}`
- Add app to settings.py installed_apps
- Start server
  - `python manage.py runserver`
  - `py manage.py runserver`