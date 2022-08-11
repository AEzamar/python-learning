emoji_dty = {
    ":)": "😄",
    ":(": "☹️",
    ":D": "😃",
    "T_T": "😢"
}
feeling = input("How are you feeling today? ")
emoji_str = ""
for char in feeling:
    emoji_str += feeling.replace(char == emoji_dty[char], emoji_dty[char])