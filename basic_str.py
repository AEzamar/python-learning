course = 'Python for Beginners'
print(len(course))
print(course.lower())
print(course.upper())
str_arr = course.split()
print(str_arr)

new_str = ''
for word in str_arr:
    new_str += word[0].upper() + word[1:] + ' '
print(new_str)
