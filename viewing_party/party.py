# ------------- WAVE 1 --------------------
from collections import defaultdict
import copy
from collections import Counter

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

#1
def get_watched_avg_rating(user_data):
    total_rating = 0 
    if not user_data["watched"]:
        avg_rating = 0.0 
    else:
        for movie in user_data["watched"]:
            total_rating += movie["rating"]
        avg_rating = total_rating/len(user_data["watched"])
    return avg_rating

#2
def get_most_watched_genre(user_data):
    #user_Data={"watched":[{"genre":a}{"genre":b}{"genre":c}]}
    genre_count ={}
    if not user_data["watched"]:
        return None
    else:
        genre_count = Counter(movie["genre"] for movie in user_data["watched"])
        most_watched_genre = genre_count.most_common(1)[0][0]     
        return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

