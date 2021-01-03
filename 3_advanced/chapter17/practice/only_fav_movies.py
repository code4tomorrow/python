"""
Charles is going to the movie today and wants
to figure out if all the movies played today
are his favorite movies. Given a set containing
the movies that are going to be played today
and a set containing all his favorite movies,
return True if all the movies played today are
his favorite. Return False otherwise. 
"""


def only_fav_movies(movies_today, favorite_movies):
    pass
    # Remove pass and write your code in here


favorite_movies = {"Home Alone", "Star Wars", "Pokemon"}
print(
    only_fav_movies({"Home Alone", "Star Wars"}, favorite_movies)
)  # Prints True
print(
    only_fav_movies({"Spider Man", "Home Alone"}, favorite_movies)
)  # Prints False
