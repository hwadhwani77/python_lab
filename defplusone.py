def plusOne(digits):
    total = 0
    for i, e in enumerate(digits[::-1]):        
        total += e * 10 ** (i)       
    return map(int, str(total + 1))

def plusOneV2(digits):
    k = -1
    while abs(k) <= len(digits) and  digits[k] == 9:
        digits[k] = 0
        k -=1
    if abs(k) > len(digits):
        digits.append(1)
        digits[0], digits[-1] = digits[-1], digits[0]
    else:
        digits[k] += 1
    return digits

l = [1,9,9]
print(list(plusOne(l)))
print(list(plusOneV2(l)))