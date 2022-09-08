def string_editor(arr):
    formatted_st = ''
    i = 1
    for st in arr:
        formatted_st += f"{i}: {st}\n"
        i += 1
    return formatted_st


print(string_editor(["Please", "Number", "These", "Strings"]))