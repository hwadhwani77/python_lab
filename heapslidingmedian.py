from heapq import *
class Solution:
    def medianSlidingWindow(self, nums, k):
        result = []
        self.maxheap = []
        self.minheap = []        
        if k <= 1:
            result = [float(x) for x in nums]
            return result
        
        result = [0.0 for x in range(len(nums) - k + 1)]
        
        for i in range(len(nums)):
            if not self.maxheap or -self.maxheap[0] >= nums[i]:
                heappush(self.maxheap, -nums[i])                
            else:
                heappush(self.minheap, nums[i])
            self.self_balance()
            
            if i - k + 1 >= 0:
                if len(self.maxheap) == len(self.minheap):
                    result[i-k+1] = -self.maxheap[0]/2.0 + self.minheap[0]/2.0
                else:
                    result[i-k+1] = -self.maxheap[0]/1.0
            
            elementToRemove = nums[i-k+1]
            if elementToRemove <= -self.maxheap[0]:
                print(i-k+1)
                self.remove_element(self.maxheap, -elementToRemove)
            else:
                self.remove_element(self.minheap, elementToRemove)
            
            self.self_balance()
        return result
    
    def remove_element(self, heap, element):
        print(element)
        index = heap.index(element)
        heap[index] = heap[-1]
        del heap[-1]
        heapify(heap)
    
    def self_balance(self):
        if len(self.maxheap) > len(self.minheap) + 1:
            heappush(self.minheap, -heappop(self.maxheap))
        elif len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, -heappop(self.minheap))
                
        
    
sol =  Solution()
sol.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3)