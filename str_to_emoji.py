emoji_dty = {
    ":)": "😄",
    ":(": "☹️",
    ":D": "😃",
    "T_T": "😢"
}
feeling = input("How are you feeling today? ")
emoji_str = ""
for str_emoji in emoji_dty:
    #print(str_emoji)
    for char in feeling:
        if char == str_emoji:
            print(feeling.replace(char, emoji_dty[char]))
            emoji_str += feeling.replace(char, emoji_dty[str_emoji])
print(emoji_str)