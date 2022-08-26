def solution(string):
    reversed_str = ""
    i = -1
    for char in string:
        print(string[-1])
    while i < len(string):
        reversed_str += string[i]
        i += 1
    return reversed_str


print(solution("Hello"))