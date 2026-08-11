class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest, smallest = nums[0], nums[0]
        maxCount = nums[0]

        for i in range(1, len(nums)):
            biggest, smallest = max(nums[i], biggest * nums[i], smallest * nums[i]), min(nums[i], biggest * nums[i], smallest * nums[i])
            maxCount = max(maxCount, biggest)

        return maxCount