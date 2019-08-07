def findDiagonalOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    row,col = len(matrix), len(matrix[0])    
    if row == 1:
        return matrix[0]
    
    i,j = 0,0
    res = []
    
    while i <= row - 1 and j <= col - 1:
        res.append(matrix[i][j])
        if (i + j) % 2 == 0:
            if i == 0  and j < col - 1:
                j += 1
            elif i == 0 and j == col - 1:
                i += 1
            elif 0 < i < row - 1 and j < col - 1:
                i -= 1
                j += 1
            elif 0 < i < row - 1 and j == col - 1:
                i += 1
            elif i == row - 1:
                i -= 1
                j += 1
        elif (i + j) % 2 == 1:
            if i == 0:
                i += 1
                j -= 1
            elif 0 < i < row - 1 and j == 0:
                i += 1
            elif 0 < i < row - 1 and j > 0:
                i += 1 
                j -= 1
            elif i == row - 1:
                j += 1
    
    return res



l = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
print(findDiagonalOrder(l))