# ------------- WAVE 1 --------------------
from collections import defaultdict
import copy

#1
def create_movie(title, genre, rating):
    movie_dic = {}
    if not title or not genre or not rating:
        return None      
    else: 
         movie_dic["title"] = title
         movie_dic["genre"] = genre
         movie_dic["rating"] = rating
         return movie_dic
#2
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

#3
def add_to_watchlist(user_data,movie):
   user_data["watchlist"].append(movie)
   return user_data

#4 
def watch_movie(user_data, title):
    user_data_copy = copy.deepcopy(user_data)
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data_copy["watchlist"].remove(movie)
            user_data_copy["watched"].append(movie)
            break
    return user_data_copy

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------







# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

