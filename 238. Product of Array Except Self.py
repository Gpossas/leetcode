class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_to_right = [1 for _ in range(len(nums))]
        for index in range(1, len(nums)):
            left_to_right[index] = nums[index-1] * left_to_right[index-1]
        
        right_to_left = [1 for _ in range(len(nums))]
        for index in range(len(nums) - 2, -1, -1):
            right_to_left[index] = nums[index+1] * right_to_left[index+1]
        
        product = []
        for index in range(len(nums)):
            product.append(left_to_right[index] * right_to_left[index])
        return product
    
class SolutionConstantSpaceComplexity:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        products = [1] * len(nums)
        previous_product = 1
        for index in range(len(nums)):
            products[index] = previous_product
            previous_product *= nums[index]
        
        posterior_product = 1
        for index in range(len(nums)-1, -1, -1):
            products[index] *= posterior_product 
            posterior_product *= nums[index]
        return products
    
print(Solution().productExceptSelf([4,3,5,2]))