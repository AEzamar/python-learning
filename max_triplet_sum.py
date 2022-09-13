def max_tri_sum(numbers):
    no_dupp_numbers = []
    for num in no_dupp_numbers:
        if num not in no_dupp_numbers:
            no_dupp_numbers.append(num)
    no_dupp_numbers.sort(reverse=True)
    n1, n2, n3 = no_dupp_numbers
    return