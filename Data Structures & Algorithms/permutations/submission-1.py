class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.combo = []
        self.seen = set()

        def backtrack():
            if len(self.combo) == len(nums):
                self.res.append(self.combo.copy())
                return
            
            for n in range(len(nums)):
                if nums[n] in self.seen:
                    continue
                
                self.seen.add(nums[n])
                self.combo.append(nums[n])

                backtrack()

                popped = self.combo.pop()
                self.seen.remove(popped)
        
        backtrack()
        return self.res
