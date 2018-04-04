# Run development server with this command
`ENV='dev' python manage.py runserver`

# Run production server with this command
`ENV='prod' python manage.py runserver`

# To create new app
`cd apps`
`../manage.py startapp my_app`

# To add new app to INSTALLED_APPS
- Open settings/base.py
- Add new app like below

`
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.my_app',
]
`
