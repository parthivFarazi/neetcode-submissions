class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i - len(word) >= 0 and dp[i - len(word)] and word == s[i - len(word): i]:
                    dp[i] = True

        return dp[-1]