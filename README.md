# Movie Recommender System

The website is being hosted at [Heroku](https://secure-bayou-21087.herokuapp.com/)

### MongoDB Collection

The mongoDB collection is stored as the file  **206_full_data.csv'**  and the user information is stored as **'206_common_users.csv'**. The former file was imported into mongodb using mongoimport :

```
mongoimport --host <MONGODB-URI> --ssl --username <USERNAME> --password <PASSWORD> --authenticationDatabase admin --db <DATABASE> --collection <COLLECTION> --type <TYPE> --file <LOCATION> --jsonArray
```

## Directory Structure

```bash
.
├── Recommending Algos
├── movie
│   ├── data
│   ├── static
│   └── templates
└── scrapper

```

A total of 6 directories are present with 27 files. The movie folder is part of the python package and helps in refactoring the code.

## Dependencies

All the required dependencies are listed in the **requirements.txt** file.

To install create a virtual environment using conda or virtualenv. Steps to follow for conda are:

```
conda create -n movie pip
source activate movie
pip install -r requirements.txt
```

This will install all the dependencies. A list of important packages used are:

```
bcrypt -> For hashing passwords
Flask  -> Backend framework in python
Flask-Login  ->  To manage user sessions
flask-mongoengine -> Relationship Manager for MongoDB
Flask-PyMongo -> Python driver for MongoDB
Flask-WTF -> Flask form management 	
```

## Code Base

The various codes in different parts of the making process are placed in different directories.

```
scrapper -> This directory contains the code for scrapping imdb Top 250 webpage along with the details
Recommending_algos -> Jupyter Notebook's with code for the collaborative filtering (item-item) and matrix factorization
```

The rest of the folder has files and directories for the website. The website has a package structure and to run the website:

```
cd <PATH_TO_FOLDER>
flask run.py
```

This will launch the server at:  [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

##  Approach Followed

#### Step 1 - Scrapping

The **ml-latest** dataset from MovieLens was used to get user ratings. The dataset had alot of movies so I decided to make my own dataset by scrapping IMDB Top 250. Movie Name, DIrector, Year , Run Time, Stars, Rating, Plot were collected and the collection is in the **movie/data folder**.

#### Step 2 - Recommending Algos

For recommendation, from the ml-latest only those users were used who had rated atleast 75 movies from IMDB Top 250. Then the codes for collaborative filtering(item-item, user-user) was written with mse of 1.89 and 2.2 achieved on using similarity of top 40 users(check recommending algos folder for code).

Matrix Factorization was done in a similar way achieving 2.1 MSE(check recommending algos folder for code).

#### Step 3 - Website

For building the website, Flask was used in the Backend along with Bootstrap for the frontend. Flask-WTF build forms for user authentication and MongoDB Atlas was used to sotre the database online.

The website has a package structure while allowed for refactoring code along with a better directory structure.

#### Step 4 - Deployment

The database was hosted on MongoDB all along so for hosting the website, heroku was chosen.

To host a flask application on heroku, first gunicorn has to be installed and a requirements.txt had to be generated. Heroku CLI has to be setup and then a Procfile has to be created in the folder.

```
pip install gunicorn
pip freeze > requirements.txt
```

Procfile:

```
web: gunicorn movie:app
```

