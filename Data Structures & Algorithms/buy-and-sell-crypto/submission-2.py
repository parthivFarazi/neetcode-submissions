class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for num in prices:
            minPrice = min(num, minPrice)
            maxProfit = max(num - minPrice, maxProfit)
        return maxProfit