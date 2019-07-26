def twoSum(arr, target):
    n = set()
    for i in arr:
        temp = target - i
        #print("Target: %d, Temp: %d" %(target, temp))
        #print(n)
        if temp in n:
            return "Yes"
        n.add(i)
    return "No"

for i in range(int(input())):
    x,y = map(int, input().split())
    arr = list(map(int, input().split()))    
    print(twoSum(arr, y))

