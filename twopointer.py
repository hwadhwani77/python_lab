import math
from collections import deque

def search_triplets(arr):
  arr.sort()
  triplets = []
  for i in range(len(arr)):
    if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
      continue
    search_pair(arr, -arr[i], i+1, triplets)

  return triplets


def search_pair(arr, target_sum, left, triplets):
  right = len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:  # found the triplet
      triplets.append([-target_sum, arr[left], arr[right]])
      left += 1
      right -= 1
      while left < right and arr[left] == arr[left - 1]:
        left += 1  # skip same element to avoid duplicate triplets
      while left < right and arr[right] == arr[right + 1]:
        right -= 1  # skip same element to avoid duplicate triplets
    elif target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum

def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    product *= arr[right]
    while (product >= target and left < len(arr)):
      product /= arr[left]
      left += 1
    # since the product of all numbers from left to right is less than the target
    # therefore, all subarrays from left to right will have a product less than the target too
    # to avoid duplicates, we will start with a subarray containing arr[right] only and extend it
    temp_list = deque()
    for i in range(right, left-1, -1):
      temp_list.appendleft(arr[i])
      result.append(list(temp_list))
  return result

def search_quadruplets(arr, target):
  arr.sort()
  quadruplets = []
  for i in range(0, len(arr)-3):
    # skip same element to avoid duplicate quadruplets
    if i > 0 and arr[i] == arr[i - 1]:
      continue
    for j in range(i + 1, len(arr)-2):
      # skip same element to avoid duplicate quadruplets
      if j > i + 1 and arr[j] == arr[j - 1]:
        continue
      search_pairs(arr, target, i, j, quadruplets)
  return quadruplets


def search_pairs(arr, target_sum, first, second, quadruplets):
  left = second + 1
  right = len(arr) - 1
  while (left < right):
    sum = arr[first] + arr[second] + arr[left] + arr[right]
    if sum == target_sum:  # found the quadruplet
      quadruplets.append(
        [arr[first], arr[second], arr[left], arr[right]])
      left += 1
      right -= 1
      while (left < right and arr[left] == arr[left - 1]):
        left += 1  # skip same element to avoid duplicate quadruplets
      while (left < right and arr[right] == arr[right + 1]):
        right -= 1  # skip same element to avoid duplicate quadruplets
    elif sum < target_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum


def backspace_compare(str1, str2):
  # use two pointer approach to compare the strings
  index1 = len(str1) - 1
  index2 = len(str2) - 1
  while (index1 >= 0 or index2 >= 0):
    i1 = get_next_valid_char_index(str1, index1)
    i2 = get_next_valid_char_index(str2, index2)
    if i1 < 0 and i2 < 0:  # reached the end of both the strings
      return True
    if i1 < 0 or i2 < 0:  # reached the end of one of the strings
      return False
    if str1[i1] != str2[i2]:  # check if the characters are equal
      return False

    index1 = i1 - 1
    index2 = i2 - 1

  return True


def get_next_valid_char_index(str, index):
  backspace_count = 0
  while (index >= 0):
    if str[index] == '#':  # found a backspace character
      backspace_count += 1
    elif backspace_count > 0:  # a non-backspace character
      backspace_count -= 1
    else:
      break

    index -= 1  # skip a backspace or a valid character

  return index

def shortest_window_sort(arr):
  low, high =  0, len(arr)-1

  while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
    low += 1
  
  if low == len(arr) - 1:
    return 0
  # print(low)
  while high > 0 and arr[high] >= arr[high-1]:
    high -= 1
  # print(high)
  s_min = math.inf
  s_max = -math.inf
  for k in range(low, high + 1):
    s_min = min(s_min, arr[k])
    s_max = max(s_max, arr[k])
  
  while low > 0 and arr[low -1] > s_min:
    low -= 1

  while high < len(arr) - 1 and arr[high + 1] < s_max:
    high += 1

  return high - low + 1
  

# print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
# print(search_triplets([-5, 2, -1, -2, 3]))
#print(find_subarrays([2, 5, 3, 10], 30))
#print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
#print(backspace_compare("xy#z", "xzz#"))
print(shortest_window_sort([3, 2, 1]))