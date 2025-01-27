class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash_nums1 = {}
        hash_nums2 = {}

        for i in nums1:
            if i in hash_nums1:
                hash_nums1[i] += 1
            else:
                hash_nums1[i] = 1

        for i in nums2:
            if i in hash_nums2:
                hash_nums2[i] += 1
            else: 
                hash_nums2[i] = 1

        answer0 = []
        for key in hash_nums1:
            if key not in hash_nums2:
                answer0.append(key)

        answer1 = []
        for key in hash_nums2:
            if key not in hash_nums1:
                answer1.append(key)

        return [answer0, answer1]