feeling = input("How are you feeling today? ")
emoji_dty = {
    ":)": "😺",
    ":(": "☹️",
    ":D": "😃",
    "T_T": "😢"
}
emoji_str = " "
char_list = feeling.split(' ')
for key in emoji_dty:
    for word in char_list:
        if word == key:
            emoji_str += feeling.replace(word, emoji_dty[word])
print(emoji_str)