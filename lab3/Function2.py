movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#Ex1
def is_high_rating(movie):
    return movie['imdb'] > 5.5
movie = {
    "name": "Dark Knight",
    "imdb": 9.0,
    "category": "Adventure"
}
result = is_high_rating(movie)
print(result) #Answer True

#Ex2
def high_rating_movies(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]
high_rating = high_rating_movies(movies)
print(high_rating)

#Ex3
def movies_by_category(category, movies):
    return [movie for movie in movies if movie['category'] == category]
category = "Romance"
romance_movies = movies_by_category(category, movies)
print(romance_movies)

#Ex4
def average_imdb_rating(movies):
    total_rating = sum(movie['imdb'] for movie in movies)
    average_rating = total_rating / len(movies)
    return average_rating
average_rating = average_imdb_rating(movies)
print("Average IMDB score", average_rating)

#Ex5
def average_imdb_rating_by_category(category, movies):
    category_movies = [movie for movie in movies if movie['category'] == category]
    total_rating = sum(movie['imdb'] for movie in category_movies)
    average_rating = total_rating / len(category_movies)
    return average_rating
category = "Romance"
average_rating = average_imdb_rating_by_category(category, movies)
print(f"Average IMDB score for category'{category}': {average_rating}")
