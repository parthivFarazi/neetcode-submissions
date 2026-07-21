class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        h = []

        for num in nums:
            if len(h) < k:
                heapq.heappush(h, num)
            else:
                if num > h[0]:
                    heapq.heappop(h)
                    heapq.heappush(h, num)
        return h[0]

        