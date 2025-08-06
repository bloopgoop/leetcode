class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        for quantity in fruits:
            for i in range(len(baskets)):
                if quantity <= baskets[i]:
                    baskets.pop(i)
                    break
        
        return len(baskets)