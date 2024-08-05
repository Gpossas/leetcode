class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        RED, BLUE = 0, 2
        red_limit = -1 # last index we find a zero
        blue_limit = len(nums) # last index we find a two(right to left)
        index = 0

        while index < blue_limit:
            if nums[index] == RED:
                red_limit += 1
                nums[index], nums[red_limit] = nums[red_limit], nums[index]
                index += 1
            elif nums[index] == BLUE:
                blue_limit -= 1
                nums[index], nums[blue_limit] = nums[blue_limit], nums[index]
            else:
                index += 1