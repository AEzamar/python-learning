emoji_dty = {
    ":)": "😺",
    ":(": "☹️",
    ":D": "😃",
    "T_T": "😢"
}
feeling = input("How are you feeling today? ")
char_list = feeling.split()
for key in emoji_dty:
    for word in char_list:
        if word == key:
            emoji = emoji_dty[key]
            