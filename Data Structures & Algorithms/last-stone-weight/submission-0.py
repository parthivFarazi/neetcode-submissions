class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        h = []

        for num in stones:
            heapq.heappush(h, -num)
        
        while len(h) > 1:
            heavy = -heapq.heappop(h)
            light = -heapq.heappop(h)

            diff = abs(heavy - light)

            if diff > 0:
                heapq.heappush(h, -diff)
            
        if len(h) == 1:
            return -h[0]
        else:
            return 0