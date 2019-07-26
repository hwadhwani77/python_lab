from collections import OrderedDict
class LRU(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
    def get(self, key):
        if key not in self:
            return -1
        
        self.move_to_end(key)
        return self[key]
    
    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if(len(self) > self.capacity):
            self.popitem(last=False)

cache = LRU(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4,4)
cache.get(1)