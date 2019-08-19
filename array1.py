def fruits_into_baskets(fruits):  
    K = 2
    if len(fruits) < 1:
        return -1
    start = 0
    max_l = 0
    dict_fruits = {}

    for i in range(len(fruits)):
        c = fruits[i]
        if c not in dict_fruits:
            dict_fruits[c] = 0
        dict_fruits[c] += 1
        while len(dict_fruits) > K:
            l = fruits[start]
            dict_fruits[l] -= 1
            if dict_fruits[l] == 0:
                del dict_fruits[l]
            start += 1
        max_l = max(max_l, i - start + 1)
    return max_l

def non_repeat_substring(str):
    if len(str) < 1:
        return -1
    max_l = 0
    start = 0
    dict_set = {}
    for i in range(len(str)):
        c = str[i]
        if c in dict_set:
            start = max(max_l, dict_set[c] + 1)        
        dict_set[c] = i            
        max_l = max(max_l, i - start + 1)
    return max_l    



#print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))

