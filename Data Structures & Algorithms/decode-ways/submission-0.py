class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            if 1 <= int(s[i - 1]) <= 9:
                a = dp[i - 1]
            else:
                a = 0

            if i > 1 and 10 <= int(s[i - 2: i]) <= 26:
                b = dp[i - 2]
            else:
                b = 0

            dp[i] = a + b

        return dp[-1]