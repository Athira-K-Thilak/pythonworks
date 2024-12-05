
movies=[{"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
        {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
        {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
        {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
        {"id":5,"title":"vazha","year":2024,"language":"malayalam","run_time":140},
        {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
        {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160}]

#count movies

print(len(movies))
#print all movies titles

movie_titles=[m.get("title") for m in movies]
print(movie_titles)
    
#movies released in 2024

movies_2024=[m.get("title") for m in movies if m.get("year")==2024]
print(movies_2024)
#malayalam movie titles

malayalam_movies=[ m.get("title") for m in movies if m.get("language")=="malayalam"]
print(malayalam_movies)

#movie with highest run time


highest_runtime_dict=(max(movies,key=lambda d:d.get("run_time")))
print(highest_runtime_dict.get("title"))

#malayalam movie count

malayalam_movie=[m.get("title") for m in movies if  m.get("language")=="malayalam"]
print(len(malayalam_movie))

#in  which year most number of movies released

all_years=[m.get("year")   for m in movies]
#[2018, 2023, 2024, 2024, 2024, 2024, 2024]
year_count={y:all_years.count(y)  for y  in all_years}
print(year_count)