class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        total_wait = 0
        cook_time = 0
        prev_arrival = customers[0][0]
        for customer in customers:
            
            cook_time -= customer[0] - prev_arrival
            if cook_time < 0:
                cook_time = 0
            prev_arrival = customer[0]

            cook_time += customer[1] # ith time
            total_wait += cook_time


        return total_wait / float(len(customers))

