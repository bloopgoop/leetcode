class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) < m + n:
            nums1 += [0 for i in range(m + n - len(nums1))]

        j = 0
        for i in range(m, m + n):
            nums1[i] = nums2[j]
            j += 1

        nums1.sort()

        return nums1