try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value, please enter a number!")