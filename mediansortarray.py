import sys

def findMedian(input1, input2):
    if(len(input1)> len(input2)):
        return findMedian(input2, input1)
    
    x = len(input1)
    y = len(input2)
    low = 0 
    high = x
    while low <= high:
        partitionX = int((low + high)/2)
        partitionY = int((x + y +1)/2 - partitionX)

        maxLeftX = sys.maxsize * -1 if partitionX ==0  else input1[partitionX- 1]
        maxLeftY = sys.maxsize * -1 if partitionY == 0  else input2[partitionY-1]

        minRightX = sys.maxsize if partitionX == x else input1[partitionX]        
        minRightY = sys.maxsize if partitionY == y else input2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if(int((x+y)% 2) == 0):
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1

def findMedianHW(a1, a2):
    if(len(a1) > len(a2)):
        return findMedianHW(a2, a1)
    
    start =  0 
    end = len(a1)    
    
    while(start <= end):
        pX = int((start + end) / 2)
        pY = int((len(a1) + len(a2) + 1)/2) - pX 

        maxX = sys.maxsize * -1 if pX == 0 else a1[pX-1] #compare with 0 index
        maxY = sys.maxsize * -1 if pY == 0 else a2[pY-1] #compare with 0 index

        minX = sys.maxsize if pX ==len(a1) else a1[pX] #compare with end index (len)
        minY = sys.maxsize if pY ==len(a2) else a2[pY] #compare with end index (len)

        if maxX <= minY and maxY <= minX:
            if(len(a1) + len(a2))%2 ==0:
                return int((max(maxX, maxY) + min(minX, minY)) /2)                
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            end = pX - 1
        else:
            start = pX + 1



    

x = [1,3,8,9,15]
y = [7,11,19,21,23,25]
print(findMedian(x,y))
print()
l = [1,3,7,8,9,11,15,18,21,25]
if(len(l) %2 == 0):
    print(l[int(len(l)/2)])
print()
print(findMedianHW(x,y))

