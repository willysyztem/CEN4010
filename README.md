# CEN4010 - Bookstore Restful API

## Index

- [Installation](https://github.com/willysyztem/CEN4010/tree/profile-management#installation)
- [Documenation](https://github.com/willysyztem/CEN4010/tree/profile-management#documentation)
- [Contributing](https://github.com/willysyztem/CEN4010/tree/profile-management#contributing)
- [Tests](https://github.com/willysyztem/CEN4010/tree/profile-management#running-tests)

## Frameworks

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgresSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## Features

API Actions

- Retrieve List of Books by Genre
- Retrieve List of Top Sellers (Top 10 books that have sold the most copied)
- Retrieve List of Books for a particular rating and higher
- Retrieve List of X Books at a time where X is an integer from a given position in the overall recordset

**Feature 2: Profile Management**

API Actions

- ✅ Create a User with username(email), password, and optional fields (name, email address, home address)
- ✅ Retrieve a User Object and its fields by their username
- ✅ Update the user and any of their fields except for email
- Create a Credit Card that belongs to a User and Retrieve a list of cards for that user

**Feature 3: Shopping Cart**

API Actions

- Create a shopping cart instance for a user. A shopping cart must belong to a user.
- Update the shopping cart with a book.
- Retrieve the list of book(s) in the shopping cart.
- Delete a book from the shopping cart instance for that user

**Feature 4: Book Details**

API Actions

- An administrator must create a book with the book ISBN, book name, book description, price, author, genre, publisher, year published, and copies sold.
- Must be able to retrieve a book’s details
- An administrator must be able to create an author with first name, last name, biography, and publisher
- Must be able to retrieve a list of books associated with an author

**Feature 5: Book Rating and Commenting**

API Actions

- Must be able to create a rating for a book by a user on a 5-star scale with a datestamp
- Must be able to create a comment for a book by a user with a datestamp
- Must be able to retrieve a list of ratings and comments sorted by highest rating
- Must be able to retrieve the average rating for a book

**Feature 6: Wish List Management**

API Actions

- Must be able to create a wishlist of books that belongs to a user and has a unique name
- Must be able to add a book to a user’s wishlist
- Must be able to remove a book from a user’s wishlist into the user’s shopping cart
- Must be able to list the book’s in a user’s wishlist

## Installation

Clone the Repo or Download the Zip File from the Repo

[ZIP](https://github.com/willysyztem/CEN4010/archive/refs/heads/main.zip) if you are lazy...

### Windows

For windows users, a `setup.bat` has been added, which will create your virtual environment for you.

![](https://i.ibb.co/zHDRw8S/setup-gif.gif)

To ensure that everything runs smoothly, please download:

- The latest [python](https://www.python.org/downloads/release/python-3102/) version
- The latest [postgreSQL](https://www.postgresql.org/download/windows/) version (windows)

**_Note: DB ISSUES_**

If you are experiencing issues with the `setup.bat` not loading correctly, you might not have configured your Database locally.
By Default, the DB Config is set to

![](https://i.ibb.co/qRWQDW6/code1.png)

If the setting is `True` will automatically use the Heroku DB.

## PLEASE USE YOUR LOCAL DB FOR TESTING!

### MAC

cd into `CEN4010`

On the terminal give permission to setup.sh to run / run the setup.sh (dont forget the dot . )

- `chmod +x setup.sh`
- `./setup.sh`

![](https://i.ibb.co/WPrRNkV/setup-mac-gif.gif)

To use in terminal 👨‍💻

- `cd CEN4010` Go inside project folder
- `python3 -m venv venv` Create your virtual environment
- `source ./venv/bin/activate/` Activate your virtual environment
- `pip install -r requirements.txt` Install dependencies
- `cd app` Go inside app folder
- `uvicorn main:app --reload` Run uvicorn server

When uvicorn is online, go to `http://127.0.0.1:8000/docs` on your browser to use SwaggerUI.

- The latest [python](https://www.python.org/downloads/release/python-3102/) version
- The latest [postgreSQL](https://www.postgresql.org/download/macosx/) version (mac)

## Documentation

Here you will find briefly what the folder structure is for our project.

![](https://i.ibb.co/5F7Z1Ck/Screen-Shot-2022-02-16-at-2-08-05-PM.png)

### App folder

In the app folder, you will find all the components that are needed for our restful API
self-explanatory.

### Config folder

In our config folder, you will find all the settings needed for our restful API, such as

**FASTAPI SETTINGS**

- `PROJECT_TITLE: str = 'Bookstore RestAPI'` Our restfulAPI title for FASTAPI
- `PROJECT_VERSION: str = '0.1.0'` Our version of our API

**DB SETTINGS**

**_CHANGE IF YOU KNOW WHAT IN THE WORLD YOU ARE DOING_**

- `POSTGRES_LOCAL: bool = True` `True` if you want to use local, `False` for Heroku
- `POSTGRES_USER: str` Postgres user most likely your machine name, Heroku is set already
- `POSTGRES_PASSWORD: str` If you set a local password, put it here, Heroku is set already
- `POSTGRES_SERVER: str` Server you created locally, Heroku is set already
- `POSTGRES_PORT: str = '5432'` Default port dont change
- `POSTGRES_DB: str` Database you created locally, Heroku is set already

### DB folder

In our DB folder, you will find our **database.py** and **models.py**

Do not touch **database.py** (skipping)

In **models.py**

Here you will introduce a new model sent over to the Database. Adding a new model will create a table based on the model.

If you need to recreate another model for the Database, copy the `User` model already created and
modify it to your needs. For extra help use [sqlalchemy](https://docs.sqlalchemy.org/en/14/orm/tutorial.html#create-a-schema) docs

### Schemas folder

In the schemas folder, you will find all the schemas that are used in FastAPI that are then
translated to the models in our DB folder.

### Main.py

`main.py` is the brains of our restful backend API; you will be adding your API endpoints here.

**_future structuring of the routers will be coming soon, to separate everyone API call_**

## Contributing

- [@Carlos Valle](https://github.com/cvall91)
- [@Richard Tubbs](https://github.com/Kedrik84)
- [@Daniel Vetan](https://github.com/danielvetan)
- [@James Vega](https://github.com/Jamesondawg)
- [@William Valido](https://www.github.com/willysyztem)
- [@Lucho Varela](https://github.com/LucianoVarela)

## Running Tests

Coming soon ...
