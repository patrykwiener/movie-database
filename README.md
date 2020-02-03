# Movie Database

## Table of Contents
* [Setup and Run](#setup-and-run)
* [Contact](#contact)

## Setup and Run
You need to have installed [Docker](https://www.docker.com/).

Clone or download the repo. Open your terminal pointing to the project root directory. To run the aplication type:

```bash
# start the server in the background
docker-compose up -d 

# apply migrations
docker-compose exec web python /code/manage.py migrate --noinput
```

If you want to walk through the application using already created accoount containing sample data, type:

```bash
# load sample data from fixture
docker-compose exec web python manage.py loaddata fixtures/sample_data.json
```
The account credentials:
* username: root
* password: root

You can also create own user by filling up the registration form or by typing:
```bash
# create superuser
docker-compose exec web python /code/manage.py createsuperuser
```

Go to http://localhost:8000/ in your browser, sign in and start using the application.

## Contact
Created by [@patrykwiener](https://github.com/patrykwiener). 

Feel free to contact me on [My LinkedIn](https://www.linkedin.com/in/patryk-wiener-439074182/)!
