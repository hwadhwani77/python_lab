def trap(height):
    ans = 0
    l = len(height)
    for i in range(l):
        max_left,max_right = 0,0
        for j in range(i, -1, -1):
            max_left = max(max_left, height[j])
        for k in range(i, l):
            max_right = max(max_right, height[k])
        ans += min(max_left, max_right) - height[i]

    return ans            

def dpTrap(height):
    ans = 0
    l = len(height)
    max_left = [0]*l
    max_right = [0]*l
    max_left[0] = height[0]
    for i in range(1, l):
        max_left[i] = max(height[i], max_left[i-1])
    max_right[l-1] = height[l-1]    
    for j in range(l-2, -1, -1):
        max_right[j] = max(height[j], max_right[j+1])
    
    for i in range(l):
        ans += min(max_left[i], max_right[i]) - height[i]
    return ans
    
l = [0,1,0,2,1,0,1,3,2,1,2,1]
#print(trap(l))
print(dpTrap(l))