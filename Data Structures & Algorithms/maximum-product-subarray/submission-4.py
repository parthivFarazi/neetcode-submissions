class Solution:
    def maxProduct(self, nums: List[int]) -> int:
            biggest, smallest = nums[0], nums[0]
            maxCount = nums[0]

            for i in range(1, len(nums)):
                biggest, smallest = max(nums[i], nums[i] * biggest, nums[i] * smallest), min(nums[i], nums[i] * biggest, nums[i] * smallest)
                maxCount = max(biggest, maxCount)

            return maxCount