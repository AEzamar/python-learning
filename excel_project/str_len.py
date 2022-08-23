def one_forty_chars(message = input("Type your message here ")):
    if message.len() > 140:
        print("Message can't be longer than 140 characters")
    else:
        print("Looks good")

one_forty_chars()