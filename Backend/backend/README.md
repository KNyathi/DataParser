# Backend
1) Create a directory called Backend and open it
```shell
mkdir backend
cd backend
```

2)  If you already have django installed, copy the code below and proceed with further instructions
```shell
django-admin startproject backend
py manage.py startapp myapp
```

3)  Go to settings and configure database settings based on the database you are using
```shell
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '.....',
        'USER': '.....',
        'PASSWORD': '....',
        'HOST': '...',
        'PORT': '5432',
    }
}
```

4) Define models in myapp, create and run migrations (Open the directory for your project)
```shell
py manage.py makemigrations
py manage.py migrate
```

5) Setup API endpoints using Django REST Framework
```shell
pip install djangorestframework
```
add rest_framework to settings.py inside your project directory

6) Install django-filter
```shell
pip install django-filter
```

Install django-cors headers

```shell
pip install django-cors-headers
```
settings.py

```shell
CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
     ...,
    'corsheaders',
]

MIDDLEWARE = [
    .....,
    'corsheaders.middleware.CorsMiddleware',
]

REST_FRAMEWORK = {
    ..., 
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.AllowAny',
    ],
}

7) Create Dockerfile for Backend
```shell
touch Dockerfile.backend
```

## All further implementations are made from within docker.
```shell
docker-compose exec backend bash
```
8) Web Scraping library used is BeautifulSoup4 for parsing data from hh.ru
```shell
pip install requests beautifulsoup4
```
9) Execute the following command to scrape data and populate the database
    ```shell
    python manage.py extract_applicants
    python manage.py extract_vacancies
    ```

 
