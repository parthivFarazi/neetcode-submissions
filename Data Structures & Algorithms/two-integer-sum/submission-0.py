class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in seen:
                return [seen[y], i]
            seen[x] = i