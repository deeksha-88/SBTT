# LeetCode 1 - Two Sum (using dictionary)
class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

# test
print(Solution().twoSum([2, 7, 11, 15], 9))
