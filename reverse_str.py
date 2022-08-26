def solution(string):
    reversed_str = ""
    i = len(string)
    while i > 0:
        reversed_str += string[i]
        i -= 1
    return reversed_str


print(solution("Hello"))