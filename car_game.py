user_input = input("> ")
help_menu = '''
start - to start the car
stop - to stop the car
quit - to exit
'''
car_started = False
while user_input.lower() != "quit":
    user_input = input("> ")
    if user_input.lower() == "help":
        print(help_menu)
    elif user_input.lower() == "start" and not car_started:
        car_started = True
        print("The car is moving!")
        if user_input.lower() == "start" and car_started == True:
            print("The is already moving")
    elif user_input.lower() == "stop" and car_started:
        print("Car has stopped")
    
