def emoji_converter(message):
    emoji_dty = {
        ":)": "😺",
        ":(": "☹️",
        ":D": "😃",
        "T_T": "😢"
    }
    emoji_str = " "
    word_list = message.split(' ')
    for word in word_list:
        emoji_str += emoji_dty.get(word, word) + " "
    return emoji_str

user_message = input("> ")
print(emoji_converter("'Ellou Gov'nor :)"))
print(emoji_converter("I'm sad Gov'nor :("))
print(emoji_converter("Thangs are dang mang :D"))
print(emoji_converter(user_message))