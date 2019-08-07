def dailyTemperatures(T):
    ans = [0] * len(T)
    s = []
    for i, value in enumerate(T):
        while s and T[s[-1]] < value:
            cur = s.pop()
            ans[cur] = i - cur
        s.append(i)
    return ans

#print(dailyTemperatures([73,74,75,71,69,72,76,73]))

def evalRPN(tokens):
    s = []
    operators = ['+', '-', '*', '/', '%']
    for t in tokens:
        if t not in operators:
            s.append(int(t))
        else:
            r, l = s.pop(), s.pop()
            if t == "+":
                s.append(l+r)            
            if t == "-":
                s.append(l-r)            
            if t == "*":
                s.append(l*r)            
            if t == "/":
                s.append(int(l/r))                            
    return s.pop()

#print(evalRPN(['1','2', '3', '/', '+']))

def numIslands(grid):    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':            
                helperDFS(i, j, grid)
                count +=1
    return count

def helperDFS(i, j, grid):
    if (i < 0) or (j < 0) or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '#'
    helperDFS(i + 1, j, grid)
    helperDFS(i - 1, j, grid)
    helperDFS(i, j + 1, grid)
    helperDFS(i, j - 1, grid)    

print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))    