class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        answer = []
        while left < right:
            if numbers[left] + numbers[right] < target:
                left = left + 1
            elif numbers[left] + numbers[right] > target:
                right = right - 1
            else:
                answer.append(left + 1) #everything is 1-indexed
                answer.append(right + 1) #everything is 1-indexed
                return answer