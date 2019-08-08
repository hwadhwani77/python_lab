def isValid(s: str):
    if len(s) < 1:
        return True
    dP = {']': '[', ')':'(', '}':'{'}
    st = []
    for x in s:
        if x in dP.values():
            st.append(x)
        elif x in dP.keys():
            if len(st) == 0 or st.pop() != dP[x]:
                return False
        else:
            return False
    return len(st) ==0

def dailyTemperatures(T):
    ans = [0] * len(T)
    stack = []
    for i, t in enumerate(T):
      while stack and T[stack[-1]] < t:
        cur = stack.pop()
        ans[cur] = i - cur
      stack.append(i)

    return ans

#print(isValid("[]"))
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))