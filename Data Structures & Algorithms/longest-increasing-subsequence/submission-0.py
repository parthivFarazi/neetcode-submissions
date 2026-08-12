class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            count = [0]
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    count.append(dp[j])
            dp[i] = 1 + max(count)
        return max(dp)
        