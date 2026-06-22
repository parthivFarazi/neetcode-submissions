class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        runLeft = 1
        for i in range(len(nums)):
            answer.append(runLeft)
            runLeft = runLeft * nums[i]
        runRight = 1
        for j in range(len(nums) - 1, -1, -1):
            answer[j] = answer[j] * runRight
            runRight = runRight * nums[j]
        return answer