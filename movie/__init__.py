from flask import Flask
# from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine, Document
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://movie:movie@vaibhav123-sx5zi.mongodb.net/recommender?retryWrites=true"
app.config['SECRET_KEY'] = 'cfea2ded4672353cac7ea5fb93bb6cf5'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# movies = mongo.db.movies.find().sort([("movieId", 1)])

from movie import routes