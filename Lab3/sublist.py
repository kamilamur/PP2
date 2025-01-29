def good_movies_list(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]