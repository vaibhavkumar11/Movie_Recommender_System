from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://movie:movie@vaibhav123-sx5zi.mongodb.net/test?retryWrites=true")
db = client.movies

# movies = [
#     {
#         'name':"The Shawshank Redemption",
#         'year':"1994",
#         'img':"https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL__QL50.jpg"
#     },
#     {
#         'name':"The Dark Knight",
#         'year':"2008",
#         'img':"https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL__QL50.jpg"
#     },
#     {
#         'name':"Schindler's List",
#         'year':"1993",
#         'img':"https://m.media-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL__QL50.jpg"
#     }
# ]


