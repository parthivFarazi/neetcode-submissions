class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        left = 1
        right = max(piles)
        result = 0

        while left <= right:

            mid = (left + right) // 2
            midH = 0
            for pile in piles:
                midH += math.ceil(pile / mid)
            
            if midH <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
