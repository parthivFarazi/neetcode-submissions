class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.combo = []

        def backtracking(i, total):

            if total == target:
                self.res.append(self.combo.copy())
                return 
            
            if i == len(nums) or total > target:
                return 

            self.combo.append(nums[i])
            backtracking(i, total + nums[i])

            self.combo.pop()

            backtracking(i + 1, total)
        
        backtracking(0, 0)
        return self.res