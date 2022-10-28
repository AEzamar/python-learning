import math
def sum_average(arr):
    #return round(reduce(lambda total, curr: total + curr, [sum(subArr) / len(subArr) for subArr in arr]))
    return math.floor(sum([sum(subArr) / len(subArr) for subArr in arr]))
    #return math.ceil(average_sum) if average_sum > .5 else math.floor(average_sum)  


print(sum_average([[1, 2, 2, 1], [2, 2, 2, 1]]))
print(sum_average([[52, 64, 84, 21, 54], [44, 87, 46, 90, 43]]))
print(sum_average([[44, 76, 12], [96, 12, 34, 53, 76, 34, 56, 86, 21], [34, 65, 34, 76, 34, 87, 34]]))
print(sum_average([[41, 16, 99, 93, 59, 18, 35, 23, 55, 45, 38, 39, 74, 60, 95, 44, 59, 70, 44, 89, 90, 19, 23, 67, 65, 66, 41, 89, 49, 22, 23, 47, 60, 12, 59, 58, 25, 69, 66, 82, 53, 41, 51, 69, 78, 18, 17, 44, 74, 96, 46, 73, 22, 37, 95, 32, 62, 49, 8, 88, 59, 66, 23, 10, 61, 28, 11, 99, 27, 98, 8, 18, 73, 18, 61, 25, 60, 38, 81, 13, 36, 63, 12, 83, 57, 11, 19, 51, 41, 20, 37, 63, 79, 94, 25, 45, 24, 73, 67, 42]]))
print(sum_average([[-4, 3, -8, -2], [2, 9, 1, -5], [-7, -2, -6, -4]]))
print(sum_average([[-91, -30, 3, -58, 88, -48, 38, -99, -100, 24], [44, 23, 70, -23, 91, 48, -37, -16, -63, 54], [54, 50, -76, -78, -46, 16, 26, 0, 7, -81, 38, 42, 33, 29, 75, 64, 21, -27, 36, -82, -70, -85, 64, -31], [33, -72, 68, -44, -76, 22, -68, 32, -58, 69, 83, -86, -58, 72, 77, 3, 74, -64, -62, -55, 80, -16, -83], [-41, -40, -71, 19, -73, 89, -97, -23, -43, -58, 38, -92, -10, 77, -57, -83, -42, 43, -75, 21, -11, -26, 35, 26], [-97, -83, 14, 78, 81, -41], [-57, 56, 65, 17, 83, 90, -30, 34, -52, 11, -66, -61, 100, -62, 18, -24, -26, -80, -7, -86], [86, -72, -15, -9, 68, 29, 37, -59, -10, 54, -65, 44, -64, -73, 62, 64, 43, 97, -75, -81], [-91, -59, -39, -4, -64, 78, -51, 18, 64, -97, -28, -80], [-98, 27, 89, -19, 55, -87, -83, 29, -29], [98, -24, -16, -13, -64, 71, 76, -96, -2, 37, -96, -100], [-91, -26, -100, 20, -65, -36, -6, 28, 100, -95, -94, 45, 32, -1, -5, -86, -94, -83, 72, -54, -85, 100, 37]]))
""" print(round(5.5))
print(round(5.1))
print(round(118.476791))
print(round(110.599999999999))
print(round(11212411233.455555982011241)) """