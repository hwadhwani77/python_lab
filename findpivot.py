def findpivot(nums):
    if len(nums) < 1:
        return -1
    l_sum = 0
    sums = sum(nums)
    for i in range(0, len(nums)):
        l_sum += nums[i]
        if sums - l_sum == l_sum - nums[i]:
            return i
    return -1

nums = [-1, -1, -1, 0, 1, 1]
print(findpivot(nums))