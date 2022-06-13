# Education  E-Learning Platform

### Table of Contents
- [Description](#description)
- [Features](#features)
- [Installing](#installing)
***
## Description
Django project,is an e-learning platform with your own content management system (CMS).
Online learning platforms are a great example of applications where you need to
provide tools to generate content with flexibility in mind. The functionality for instructors to create courses and manage the contents of courses in a versatile and efficient manner.
***
## Features
- Content management system (CMS), using model inheritance and custom model fields, and different groups permissions.
- Fixtures for models.
- Class-based views and mixins.
- Formsets.
- Public views for displaying course information.
- A student registration system and courses student enrollment.
- Memcache and cache content using the Django cache framework.
- Monitor Memcached using the django-memcache-status.
- Caching dynamic data,  template fragment,  view and pre-site cache.
- RESTful API.
- Custom API views.
- API views  permissions.
- Settings for multiple environment.
***
## Installing

Clone the project:
```
git clone https://github.com/davkdev620/education.git
```

Install the requirements.txt file:
```
pip install -r requirements.txt
```

Make migration:
```
python manage.py makemigrations
python manage.py migrate
```

Crate super user:
```
python manage.py createsuperuser
```
Add content.

Collect static files:
```
python manage.py collectstatic
```


Installing Memcached:

* download: https://memcached.org/downloads

Linux:
```
./configure && make && make test && sudo make install
```

For MacOS:
* https://brew.sh/

For Windows:
* Switch your OS to linux or macOS.


Open shell and run:
```
memcached -l 127.0.0.1:11211
```

Open in your browser to monitoring memcached: 
* http://127.0.0.1:8000/admin/


#### API
Open the shell and retrieve the URL http://127.0.0.1:8000/api/subjects/ with curl, as follows:
```
curl http://127.0.0.1:8000/api/subjects/
```

To obtain a more readable, well-indented JSON response, you can use curl with
the json_pp utility, as follows:
```
curl http://127.0.0.1:8000/api/subjects/ | json_pp
```

Open http://127.0.0.1:8000/api/subjects/ in your browser.

Open http://127.0.0.1:8000/api/subjects/1/ in your browser. You will see a
single Subject object rendered in JSON format.

You can access http://127.0.0.1:8000/api/courses/ to retrieve the list of
courses.

Open http://127.0.0.1:8000/api/courses/1/contents/ in your browser.
If you access the view with the right credentials, you will see that each module
of the course includes the rendered HTML for course contents.


#### To run the app (3 options):
1. Set a DJANGO_SETTINGS_MODULE environment variable:

    Open the shell and run the following command:
    ```
    export DJANGO_SETTINGS_MODULE=education.settings.production
    
    python manage.py shell –settings=education.settings.production
    ```
    Then run:
    ```
    python manage.py runserver
    ```
   <br>

2. 
    for production use:
    ```
    python manage.py runserver –settings=education.settings.production
    ```
    for local use: 
    ```
    python manage.py runserver –settings=education.settings.local
    ```   

3. Or set at .bashrc local variables.
    And then run:
    ```
    python manage.py runserver
    ```
   

#### PostgreSQL Settings.
Create a PostgreSQL user. Open the shell and run the following commands to
create a database user:
```
su postgres
createuser -dP education
```
Create a new database with the following command:
```
createdb -E utf8 -U education education
```
* Edit the settings in settings/production.py


___Checking project before deploy:___
```
python manage.py check –deploy
```

___Before usage config and edit education/settings/producion.py and set your email.___ 

__For production use, before publish the project, change the SECRET_KEY. It’s recommended to set it as local variable!__ 


