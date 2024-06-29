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
   ```shell
   npm start
   ```
6) Axios is used to connect frontend to backend
- URL: This is the URL of the *hh.ru* page we want to scrape. It searches for Python jobs in Moscow.
- BeautifulSoup: It parses the HTML response from the URL.
- Vacancy Model: The script creates or updates Vacancy objects in our Django database based on the scraped data. It checks if a Vacancy with the same title and company exists and updates its fields if it does, or creates a new one if it doesn't.
- Applicant Model: The script creates or retrieves an Applicant object based on hardcoded applicant data (applicant_data).
- Linking: It links each applicant to the corresponding vacancy they apply for using vacancy_obj.applicants.add(applicant_obj).

9) Further instructions are available on each directory for both Frontend and Backend.
