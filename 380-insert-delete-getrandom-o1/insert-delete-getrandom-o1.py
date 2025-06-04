import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        
        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.map:
            return False
        
        # update the val in the arr to be the last val of the arr
        # val = 1
        # [1, 2, 3, 4] -> [4, 2, 3, 4]
        index = self.map[val]
        self.arr[index] = self.arr[-1]

        # update map to point to val's index
        # val = 1
        # self.map[4] -> 0
        self.map[self.arr[-1]] = index

        # del last item in arr and del the val from map
        self.arr.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()