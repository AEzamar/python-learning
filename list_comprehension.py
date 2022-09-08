def g_movies(lst): 
    return [mov for mov in lst if mov.startswith('G')]


print(g_movies(["Frankenstein", "Old Gals", "The Matrix", "Gattaca", "Gulliver", "Sausage Party"]))