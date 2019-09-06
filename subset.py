from collections import deque
def find_subsets(nums):
  subsets = []
  # start by adding the empty subset
  subsets.append([])
  for currentNumber in nums:
    # we will take all existing subsets and insert the current number in them to create new subsets
    n = len(subsets)
    for i in range(n):
      # create a new subset from the existing subset and insert the current element to it
      set = list(subsets[i])
      set.append(currentNumber)
      subsets.append(set)

  return subsets


def find_subsets_dup(nums):
    subsets = []
    # start by adding the empty subset
    subsets.append([])  
    nums.sort()
    start, end  = 0,0
    for i in range(len(nums)):
        start = 0      
        if i > 0 and nums[i] == nums[i-1]: #handle duplicate  
            start = end +1
        end = len(subsets) - 1                                        
        for k in range(start, end + 1):
            s = (list(subsets[k]))
            s.append(nums[i])
            subsets.append(s)

    return subsets

def find_permutations(nums):
    result = []
    nLength= len(nums)
    permutations = deque()
    permutations.append([])
    for num in nums:
        n = len(permutations)
        for _ in range(n):
            oPermutation = permutations.popleft()
            for j in range(len(oPermutation) + 1):
                nPermutation = list(oPermutation)
                nPermutation.insert(j, num)
                if len(nPermutation) == nLength:
                    result.append(nPermutation)
                else:
                    permutations.append(nPermutation)        
    return result

print(find_subsets([1,3,5]))
print(find_subsets_dup([1,3,3,1,5]))
print(find_permutations([1,2,3]))