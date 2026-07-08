class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        aList = sorted(nums)
        for i in range(len(aList)):
            
            if i > 0 and aList[i] == aList[i - 1]:
                continue
            
            target = 0 - aList[i]

            left = i + 1
            right = len(aList) - 1

            while left < right:

                if aList[left] + aList[right] == target:
                    answer.append([aList[i], aList[left], aList[right]])
                    left = left + 1
                    right = right - 1
                    while left < right and aList[left - 1] == aList[left]:
                        left = left + 1

                elif aList[left] + aList[right] > target:
                    right = right - 1

                elif aList[left] + aList[right] < target:
                    left = left + 1

    
        return answer                    