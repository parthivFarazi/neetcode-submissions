class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.path = []

        def backtrack(i):
            if i == len(nums):
                self.res.append(self.path.copy())
                return

            self.path.append(nums[i])
            backtrack(i + 1)

            self.path.pop()

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i = i + 1
            backtrack(i + 1)
        
        backtrack(0)
        return self.res

        