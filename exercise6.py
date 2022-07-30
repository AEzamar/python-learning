user_name = str(input("Create a user name "))
if len(user_name) < 5:
    print("Please make your username at least 5 characters long")
elif len(user_name) > 50:
    print("Your username can't be longer than 50 characters")
else:
    print("Valid username registered!")