class RecentCounter:

    def __init__(self):
        self.TIME_FRAME = 3000
        self.recent_requests = []

    def ping(self, t: int) -> int:
        min_time = t - self.TIME_FRAME
        self.recent_requests.append(t)
        while self.recent_requests[0] < min_time:
            self.recent_requests.pop(0)
        return len(self.recent_requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)