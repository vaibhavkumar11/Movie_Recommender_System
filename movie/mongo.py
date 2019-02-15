from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://movie:movie@vaibhav123-sx5zi.mongodb.net/test?retryWrites=true")
db = client.recommender

movies = db.movies.find({}).sort([("movieId", 1)])
for movie in movies:
    print(movie['title'])


