def largest_pair_sum(numbers):
    sorted_lst = sorted(numbers, reverse=True)
    return sum(sorted_lst[0:2])


print(largest_pair_sum([10,14,2,23,19]))
print(largest_pair_sum([-100,-29,-24,-19,19]))
print(largest_pair_sum([1, 2, 3, 4, 6, -1, 2]))