def g_movies(lst): 
    return [mov for mov in lst if mov.startswith('G')]


print(g_movies(["Frankenstein", "Old Gals", "The Matrix", "Gattaca", "Gulliver", "Sausage Party"]))

def two_thousand_movies(lst):
    return [title for (title, year) in lst if year < 2000] 


print(two_thousand_movies([('The Matrix', 1999), ('Ernest Goes Full MAGA', 2016), ('American Psycho', 2003), ('Amelie', 1998)]))


def scalar_multiplication(lst):
    return [num * 4 for num in lst]


print(scalar_multiplication([2, -3, 1]))


def cartesian_product(list_a, list_b):
    return [(a, b) for a in list_a for b in list_b]