def find_average(nums):
    avg = 0
    for num in nums:
        avg += num
    return 0 if nums == [] else avg / len(nums)


print(find_average([9, 8, 9, 9, 9, 9, 9, 9]))
print(find_average([]))