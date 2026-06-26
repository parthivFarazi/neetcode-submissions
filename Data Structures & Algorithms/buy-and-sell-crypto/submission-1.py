class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for num in prices:
            if num < minPrice:
                minPrice = num
            
            if num - minPrice > maxProfit:
                maxProfit = num - minPrice

        return maxProfit