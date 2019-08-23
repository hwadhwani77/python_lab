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

def find_permutation(str, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in char_frequency:
      # decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):
      return True

    # shrink the window by one character
    if window_end >= len(pattern) - 1:
      left_char = str[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  return False

def find_string_anagrams(str, pattern):
    result_indexes = []
    match = 0
    start = 0
    dict_map = {}
    for p in pattern:
        if p not in dict_map:
            dict_map[p] = 0
        dict_map[p] += 1

    for i in range(len(str)):
        l = str[i]
        if l in dict_map:
            dict_map[l] -= 1
            if dict_map[l] == 0:
                match += 1
        if match == len(pattern):
            result_indexes.append(start)
        
        if i >= len(pattern) - 1:
            c = str[start]
            start += 1
            if c in dict_map:
                if dict_map[c] == 0:
                    match -=1
                dict_map[c] += 1

    return result_indexes

def find_permutation2(str, pattern):
  window_start, matched, substr_start = 0, 0, 0
  min_length = len(str) + 1
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # try to extend the range [window_start, window_end]
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in char_frequency:
      char_frequency[right_char] -= 1
      if char_frequency[right_char] >= 0:  # Count every matching of a character
        matched += 1

    # Shrink the window if we can, finish as soon as we remove a matched character
    while matched == len(pattern):
      if min_length > window_end - window_start + 1:
        min_length = window_end - window_start + 1
        substr_start = window_start

      left_char = str[window_start]
      window_start += 1
      if left_char in char_frequency:
        # Note that we could have redundant matching characters, therefore we'll decrement the
        # matched count only when the last occurrence of a matched character is going out of the window
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  if min_length > len(str):
    return ""
  return str[substr_start:substr_start + min_length]    
#print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
#print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
#print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))
#print(find_string_anagrams("ppqp", "pq"))
print(find_permutation2("aabdec", "abc"))