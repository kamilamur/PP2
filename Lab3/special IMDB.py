movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]


def is_good_movie(movie):
    return movie['imdb'] > 5.5

def good_movies_list(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

def movies_by_category(movies, category):
    return [movie for movie in movies if movie['category'] == category]

def average_imdb_score(movies):
    if not movies:
        return 0  
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)

def average_imdb_for_category(movies, category):
    category_movies = [movie for movie in movies if movie['category'] == category]
    return average_imdb_score(category_movies)

print("Good Movies:", good_movies_list(movies))
print("Movies in Romance Category:", movies_by_category(movies, "Romance"))
print("Average IMDB Score:", average_imdb_score(movies))
print("Average IMDB for Romance Movies:", average_imdb_for_category(movies, "Romance"))