def find_average(nums):
    avg = 0
    for num in nums:
        avg += num
    return 0 if nums == [] else avg / len(nums)


print(find_average([9, 8, 9, 9, 9, 9, 9, 9]))
print(find_average([]))


#This solution is user submitted, dang!
""" def find_average(nums):
    return float(sum(nums)) / len(nums) if len(nums) !=0 else 0 """