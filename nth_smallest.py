def nth_smallest(arr, pos):
    return sorted(arr)[pos - 1]


print(nth_smallest([3,1,2], 2))
print(nth_smallest([15,20,7,10,4,3], 3))
print(nth_smallest([-5,-1,-6,-18], 4))


#User submitted solution
#Never used this module before, have to look it up
""" from heapq import nthsmallest
def nth_smallest(arr, pos):
    return nthsmallest(pos, arr)[-1] """