help_menu = '''
[start - to start the car]
[stop - to stop the car]
[quit - to exit]
'''
car_started = False
user_input = ""
while user_input != "quit":
    user_input = input("> ").lower()
    if user_input == "help":
        print(help_menu)
    elif user_input == "start" and not car_started:
        print("The car is moving!")
        car_started = True
    elif user_input == "start" and car_started == True:
            print("The car is already moving")
    elif user_input == "stop" and car_started:
        print("The car has stopped")
        car_started = False
    elif user_input == "stop" and car_started == False:
            print("The car has already stopped!")
