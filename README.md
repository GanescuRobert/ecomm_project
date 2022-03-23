# [Django ecommerce project](https://www.youtube.com/playlist?list=PL_99hMDlL4d2zsGU5nOgADmRc6A8msXyh)

## Setup environment

- Anaconda
  - conda create --prefix ./env/"name of environment (without spaces)" python=3.8
  - conda config --append envs_dirs "absolute path"/env/
  - conda activate "name of environment (without spaces)"
  - pip install -r requirements.txt
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

## Create app

- python manage.py startapp store
- Append 'store' in ecomm_shop/settings.py

  ```text
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store'
  ]
  ```

- In **store** create 'urls.py'
- Append store/urls.py in ecomm_shop/urls.py

## Make migrations

After creating the classes, the migrations must be made:

- `python manage.py makemigrations`
- `python manage.py migrate`

## Create super user

The following command must be run to create an admin:

- `python manage.py createsuperuser`
