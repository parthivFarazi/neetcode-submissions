class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## Not Optimized O(n) space complexity
        left = []
        runLeft = 1
        for i in range(len(nums)):
            left.append(runLeft)
            runLeft = runLeft * nums[i]

        rightRev = []
        runRight = 1
        for j in range(len(nums) - 1, -1, -1):
            rightRev.append(runRight)
            runRight = runRight * nums[j]
        right = rightRev[::-1]
        
        final = []
        for k in range(len(nums)):
            value = left[k] * right[k]
            final.append(value)
        
        return final
