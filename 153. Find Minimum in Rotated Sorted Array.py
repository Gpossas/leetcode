class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            lower_bound = ( left + right ) >> 1

            if (
                nums[left] <= nums[lower_bound] 
                and nums[right] < nums[left]
            ):
                left = lower_bound + 1
            else:
                right = lower_bound
        return nums[left]