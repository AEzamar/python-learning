def greet_user(f_name, l_name):
    print(f"Hello {f_name} {l_name}!")
    print("Welcome aboard")


#Keyword arguments
greet_user(l_name="Smith", f_name="John") #This is another way to do positional arguments and it's called keyword arguments were instead of relying on position you tell python what argument belongs to what parameter
greet_user("Mary", "Schmary") 