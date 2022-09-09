def find_average(nums):
    avg = 0
    for num in nums:
        avg += num
    return avg / len(nums)


print(find_average([9, 8, 9.5, 9.2, 9.1, 9.4, 9.1, 9.5]))