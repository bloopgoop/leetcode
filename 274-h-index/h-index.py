class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n = len(citations)

        h = 0
        for i, num in enumerate(citations):
            h = max(h, min(i + 1, num))
            if i + 1 >= num:
                return h
        
        return n