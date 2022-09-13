def max_tri_sum(numbers):
    no_dupp_numbers = []
    for num in numbers:
        if num not in no_dupp_numbers:
            no_dupp_numbers.append(num)
    print(no_dupp_numbers)
    no_dupp_numbers.sort(reverse=True)
    n1, n2, n3 = no_dupp_numbers
    return n1 + n2 + n3


print(max_tri_sum([3,2,6,8,2,3]))