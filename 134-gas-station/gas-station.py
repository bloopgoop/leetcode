class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        # Assume this case
        # i = 0, success <- start
        # i = 1, success
        # i = 2, success
        # i = 3, success
        # i = 4, fail

        # when start = 0,
        # let s0 = surplus at i = 0
        # gas[i] - cost[i] = ti
        # let b = (1i + 2i + 3i + 4i) 
        # s0 + b < 0
        # s0 < -b
        
        # 1i + 2i + 3i + 4i will be negative and 4i is negative
        # that means we should not check this range because no matter where we start,
        # the tank will always be negative
        # therefore, when i = 4 and tank falls below 0, it is sufficient to assign i + 1 to start

        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1

        return start