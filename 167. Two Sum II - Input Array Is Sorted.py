class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            _sum = numbers[left] + numbers[right]
            if _sum < target:
                left += 1
            elif _sum > target:
                right -= 1
            else:
                return (left + 1, right + 1)