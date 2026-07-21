class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k

        for num in nums:
            if len(self.h) < self.k:
                heapq.heappush(self.h, num)
            else:
                if num > self.h[0]:
                    heapq.heappop(self.h)
                    heapq.heappush(self.h, num)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        else:
            if val > self.h[0]:
                heapq.heappop(self.h)
                heapq.heappush(self.h, val)
        return self.h[0]
        
