class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            least = float('inf')
            for n in coins:
                if i - n >= 0:
                    least = min(least, 1 + dp[i - n])
            dp[i] = least

        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]