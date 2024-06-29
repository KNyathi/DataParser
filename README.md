# DataParser

## The application was developed using Django framework for Backend and React Framework for Frontend. The Database used is PostGreSQL. 

## Key Points
1) Clone the repository using the command below
   ```shell
   git clone ....
   ```
2) Ensure you have Docker running in your system and run the command below
```shell
docker-compose up --build
```

This will start the PostgreSQL database, Django Backend, and React Frontend in separate containers.

3) Backend is running in port 8000 and Frontend in 3000. You may adjust the ports to fit your preferences.

### Datasource is hh.ru and we are using BeautifulSoap for parsing data.

4) To access the backend shell from within docker, type the command below
```shell
docker-compose exec backend bash
```
To make migrations, you can then type
```shell
python manage.py migrate
```
5) To access the frontend shell from within docker, type the command below
   ```shell
   docker-compose exec frontend bash
   ```
6) Further instructions are available on each directory for both Frontend and Backend.
