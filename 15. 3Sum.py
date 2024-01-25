class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        left, right = 0, len(nums) - 1
        triplets = set()
        while left < right:
            complement = -(nums[right] - nums[left])

            # Search for complement using Binary Search
            if self.binary_search(complement, left + 1, right - 1, nums):
                triplets.add((nums[left], nums[complement], nums[right]))
                # if found, remove any left or right 
                right -= 1
            elif complement < 0:
                right -= 1
            else:
                left += 1

        return list(triplets)


    def binary_search(self, target, left, right, nums):
        while left <= right:
            middle = left + (right - left) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                return True
        return False