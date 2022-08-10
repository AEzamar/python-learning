user = {
    "name": "Ed",
    "email": "ed@edmail.com",
    "Phone#": "7221596770"
}
name = user["name"]
#If we try to access an unexistent key with .get() we onyl get none
#instead of crashing the whole script
print(user.get("birthdate"))
#print(user.get("birthdate", "Feb 14 1988")) #This way we can define a key/value pair if it doesn't exist
for key in user:
    print(user[key])
#Re-assigning a value to a key
user["name"] = "Ed Azamar"
print(name)
