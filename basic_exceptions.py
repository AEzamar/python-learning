try:
    age = int(input("Age: "))
    income = 20000
    risk = income /age
    print(age)
except ZeroDivisionError:
    print("The input for age cannot be zero!")
except ValueError:
    print("Invalid value, please enter a number!")