course = 'Python for Beginners'
print(len(course))
print(course.lower())
print(course.upper())
str_arr = course.split()
print(str_arr)

for word in str_arr:
    print(word[0].upper() + word[1:])
