weight = int(input("What is your weight? "))
w_unit = input("(L)bs or (K)g: ")
if(w_unit.lower() == "l"):
    print(f"Your weight in Kilograms is: {weight * 0.45} kg")
elif(w_unit.lower() == "k"):
    print(f"Your weight in Pounds is: {weight / 0.45} lbs")