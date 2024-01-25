class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            # lower bound middle
            middle = (left + right) >> 1

            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle
        return left if nums[left] == target else -1
    
print(Solution().search([-1,0,3,5,9,12], 9))