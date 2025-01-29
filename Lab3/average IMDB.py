def average_imdb_score(movies):
    if not movies:
        return 0  
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)