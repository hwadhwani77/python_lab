def maxSubArray(nums): # O(nsquare)
    if(len(nums) < 1):
        return 0
    maxV = nums[0]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)-1):
            t = nums[i] + nums[j]
            if maxV > t:
                continue
            else:
                maxV = t
                break
    return maxV

def maxSubArray2(nums): #O(n)
    if len(nums)< 1:
        return 0
    maxV = nums[0]
    for i in range(1, len(nums)):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
            maxV = max(nums[i], maxV)
    return maxV


l = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(l))
print(maxSubArray2(l))