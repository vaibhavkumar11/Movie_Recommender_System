# Movie Recommender System

The website is being hosted at [Heroku](https://secure-bayou-21087.herokuapp.com/)

### MongoDB Collection

The mongoDB collection is stored as the file  **206_full_data.csv'**  and the user information is stored as **'206_common_users.csv'**. The former file was imported into mongodb using mongoimport :

```
mongoimport --host vaibhav123-shard-0/vaibhav123-shard-00-00-sx5zi.mongodb.net:27017,vaibhav123-shard-00-01-sx5zi.mongodb.net:27017,vaibhav123-shard-00-02-sx5zi.mongodb.net:27017 --ssl --username <USERNAME> --password <PASSWORD> --authenticationDatabase admin --db <DATABASE> --collection <COLLECTION> --type <TYPE> --file <LOCATION> --jsonArray
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

All the required dependencies are listed in the requirements.