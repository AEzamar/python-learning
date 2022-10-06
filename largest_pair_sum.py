def largest_pair_sum(numbers):
    #sorted(numbers, reverse=True)
    return [num for num in sorted(numbers, reverse=True)] 

print(largest_pair_sum([10,14,2,23,19]))