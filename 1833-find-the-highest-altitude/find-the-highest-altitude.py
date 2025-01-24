class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        altitude = 0
        for i in gain:
            altitude += i
            res = max(res, altitude)
        return res