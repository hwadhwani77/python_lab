from collections import OrderedDict
# l =[2, 7, 11, 15]
# d = {e: i for i,e in enumerate(l)}
# print(d)

def twoSum(nums,target):
    ans = []
    d = {}
    f = False
    for i in range(0, len(nums)):
        t = target - nums[i]
        if t in d.values():
            for k,v in d.items():
                if v == t and k != i:
                    ans.append(k)
                    ans.append(i)
                    f = True
                    break; 
            if f:
                break
        else:
            d[i] = nums[i]      
    return ans

l = [3,2,4]
print(twoSum(l, 6))