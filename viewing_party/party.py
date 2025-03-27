# ------------- WAVE 1 --------------------
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
def get_unique_watched(user_data):
    #the list of movies the user has watched
    user_watched = user_data["watched"]

    # List that friend is watched(titles)
    friends_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie["title"])
    #store the movies that only the user has watched
    unique_movies = []

    for movie in user_watched:
        if movie["title"] not in friends_watched:
        #checking if the movie is not in friends' watched list, add to result
            unique_movies.append(movie)
    #list that user watched
    return unique_movies

#2
def get_friends_unique_watched(user_data):
    # list of movies the user has watched
    user_watched = user_data["watched"]
    # Get the list of friends
    friends = user_data["friends"]

    user_titles = []
    for movie in user_watched:
        user_titles.append(movie["title"])
    
    #Store unique movies friends have watched
    friends_unique = []

    seen_titles = set()

    for friend in friends:
        for movie in friend["watched"]:
            title = movie["title"]

            # If the user hasn't watched it and it's not already added
            if title not in user_titles and title not in seen_titles:
                friends_unique.append(movie)
                # Title that seen to avoid duplicates
                seen_titles.add(title)

    #list that friends watched
    return friends_unique
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    # Step 1: Get a list of movies that friends have watched, with no duplicate titles
    friend_watched_list = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched_list.add(movie["title"])
    
    # Step 2: Filter out movies that the user has already watched
    user_watched_list = set()
    for movie in user_data["watched"]:
        user_watched_list.add(movie["title"])

    friend_watched_user_not_list = []
    for title in friend_watched_list:
        if title not in user_watched_list:
            friend_watched_user_not_list.append(title)

    # Step 3: From the remaining movies, find those hosted on platforms the user subscribes to
    movie_in_host = []
    for friend in user_data ["friends"]:
        for movie in friend["watched"]:
            if (movie["title"] in friend_watched_user_not_list 
                and movie["host"] in user_data["subscriptions"] 
                and movie not in movie_in_host):
                movie_in_host.append(movie)
    return movie_in_host

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

