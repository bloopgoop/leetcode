class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        return sorted(nums, key=lambda x:(freq[x], -x))


