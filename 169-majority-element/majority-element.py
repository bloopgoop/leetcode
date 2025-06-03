class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer–Moore_majority_vote_algorithm
        m = nums[0]
        c = 0
        for x in nums:
            if c == 0:
                m = x
                c = 1
            elif m == x:
                c += 1
            else:
                c -= 1
        return m
