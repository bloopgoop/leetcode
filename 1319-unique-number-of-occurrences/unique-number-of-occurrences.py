class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in arr:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        occurences = []
        for key in count:
            if count[key] in occurences:
                return False
            else:
                occurences.append(count[key])

        return True