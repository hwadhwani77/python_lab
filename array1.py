import math
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

def length_of_longest_substring(str, k):
    # TODO: Write your code here
    if len(str) < 1:
        return -1

    start, max_l, max_letter_count = 0,0,0
    dict_map = {}
    for i in range(len(str)):
        l = str[i]
        if l not in dict_map:
            dict_map[l] = 0
        dict_map[l] += 1
        max_letter_count = max(max_letter_count, dict_map[l])

        if(i- start + 1 - max_letter_count) > k:
            f = str[start]
            dict_map[f] -= 1
            start += 1
        max_l = max(max_l, i - start + 1)
    return max_l

def length_of_longest_substring1(arr, k):
    start, max_l, max_one_count = 0,0,0
    
    for i in range(len(arr)):
        if arr[i] == 1:
            max_one_count +=1
        
        if i - start + 1 - max_one_count > k:
            if arr[start] == 1:
                max_one_count -= 1
            start += 1
        max_l = max(max_l, i - start + 1)
    return max_l



def triplet_sum_close_to_target(arr, target_sum):
    smallest = math.inf
    arr.sort()
    for i in range(len(arr) - 2):
        left = i+1
        right = len(arr) - 1 
        while left < right:
            t_diff = target_sum - arr[i] - arr[left] - arr[right]
            if t_diff == 0:
                return target_sum - t_diff
            if abs(t_diff) < abs(smallest):
                smallest = t_diff
            if t_diff > 0:
                left +=1
            else:
                right -= 1
    return target_sum - smallest

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        count += searchPair(arr, target-arr[i], i)
    return count

def searchPair(arr, target_sum, first):
    left = first + 1
    right = len(arr) - 1
    count = 0
    while left < right:
        if arr[left] + arr[right] < target_sum:
            count += right - left
            left += 1
        else:
            right =-1
    return count


#print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
#print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
#print(length_of_longest_substring("abccde", 1))
#print(length_of_longest_substring1([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
#print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))


