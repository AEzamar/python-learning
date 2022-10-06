def largest_pair_sum(numbers):
    sorted_lst = sorted(numbers, reverse=True)
    return sum(sorted_lst[0:2])


print(largest_pair_sum([10,14,2,23,19]))