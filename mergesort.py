def mergesort(nums):
    if len(nums) <= 1:
        return nums
    p = int(len(nums)/2)
    l_list = mergesort(nums[:p])
    r_list = mergesort(nums[p:])
    return merge(l_list, r_list)

def merge(l, r):
    l_cur = r_cur = 0
    ret = []
    while(l_cur < len(l) and r_cur < len(r)):
        if l[l_cur] < r[r_cur]:
            ret.append(l[l_cur])
            l_cur += 1
        else:
            ret.append(r[r_cur])
            r_cur += 1
    
    ret.extend(l[l_cur:])
    ret.extend(r[r_cur:])
    return ret

l = [2, 5, 3, 88, 3, 34, 12, 45, 56]
print(mergesort(l))