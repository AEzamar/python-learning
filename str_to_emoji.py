emoji_dty = {
    ":)": "😺",
    ":(": "☹️",
    ":D": "😃",
    "T_T": "😢"
}
print(emoji_dty[":)"])
emoji = ""
feeling = input("How are you feeling today? ")
for key in emoji_dty:
    for char in feeling:
        print(char)
            