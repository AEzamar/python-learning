emoji_dty = {
    ":)": "😄",
    ":(": "☹️",
    ":D": "😃",
    "T_T": "😢"
}
feeling = input("How are you feeling today? ")
for char in feeling:
    emoji = emoji_dty.get(char)
print(emoji)