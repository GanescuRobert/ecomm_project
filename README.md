# ecomm_project

## Setup environment

- Anaconda
  - conda create --prefix ./env/"name of environment (without spaces)" python=3.8
  - conda config --append envs_dirs "absolute path"/env/
  - conda activate "name of environment (without spaces)"
  - pip install django
  - pip install mysqlclient
  - django-admin startproject "name of project (without spaces)"
- XAMPP

  - You have to create a database and in the file 'setting.py' set this:

  ```text
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<name of the database (without spaces)>',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
        'PORT': '3306',
    }
  }
  ```

## Run project

```text
python manage.py runserver
```
