class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []

        def backtracking(i):

            if i == len(nums):
                self.res.append(self.path.copy())
                return
            
            self.path.append(nums[i])
            backtracking(i + 1)
            self.path.pop()

            backtracking(i + 1)
        
        backtracking(0)
        return self.res
        