# count the frequency, if any value >= 2 -> duplicate
def contains_duplicate(nums):
    freq = {}
    count = 0
    for i in nums:
        freq[i] = freq.get(i, 0) + 1
    for key, value in freq.items():
        if value >= 2:
            count += 1
    if count >= 1:
        return True
    else:
        return False


nums = list(map(int, input().split(",")))
print(contains_duplicate(nums))
