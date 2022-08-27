def solution(string):
    reversed = ""
    i = -1
    for char in string:
        reversed += string[i]
        i += -1
    return reversed


print(solution("Hello"))
print(solution("World"))
print(solution("Reverse This!"))


#There is a one line solution to this
def solution1(string):
    return string[:: -1]


print(solution1("Damn"))