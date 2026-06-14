import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    print(cinema.index)
    result = cinema[(cinema.index % 2 == 0) & (cinema["description"] != "boring")]
    result_sort = result.sort_values('rating', ascending=False)
    return result_sort


cinema_data = {
    'id' : [1, 2, 3, 4, 5],
    'movie': ["War", "Science", "irish", "Ice song", "House card"], 
    'description' : ['great 3D', 'fiction', 'boring', 'Fantacy', 'Interesting'],
    'rating' : [8.9, 8.5, 6.2, 8.6, 9.1]
}

cinema = pd.DataFrame(cinema_data)
getAnsw = not_boring_movies(cinema)
print(getAnsw)