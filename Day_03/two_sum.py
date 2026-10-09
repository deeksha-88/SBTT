# 2Sum - optimized approach: dictionary (hash map)
def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]    # index
        d[num] = i


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
