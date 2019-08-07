import math
# move = {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
# print(move)

# q = ["0000"]
# for s in q:
#     for i,c in enumerate(s):
#         if i ==0:
#             print("i: %d, c: %s" %(i,c))
#             print("S[:i]: %s" %(s[:i]))
#             print("S[i+1:]: %s" %(s[i+1:]))
#             print(move[c][0])
#             print(s[:i]+ move[c][0] + s[i+1:])
#             print(s[:i]+ move[c][1] + s[i+1:])


def numSquares(n):
    if n < 2:
        return n

    lst = []
    i = 1
    while i * i <= n:
        lst.append(i * i)
        i +=1
    print(lst)    
    cnt = 0
    c = {n}
    while c:
        cnt += 1
        temp = set()
        for x in c:
            for y in lst:
                if x == y:
                    return cnt
                elif x < y:
                    break
                temp.add(x-y)
        c = temp
    return cnt
        

print(numSquares(13))
