def solution(string):
    reversed = ""
    i = -1
    for char in string:
        reversed += string[i]
        i += -1
    return reversed

    
print(solution("Hello"))