from pymongo import MongoClient
from pprint import pprint

client = MongoClient("")
db = client.recommender

movies = db.movies.find({}).sort([("movieId", 1)])
for movie in movies:
    print(movie['title'])


