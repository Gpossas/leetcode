class Solution:
    # a ideia é saber se left até mid está em ordem, se estiver posso usar binary search para ver se target está entre eles
    # se não estiver ordenado, não podemos comparar os valores para saber se target está entre left e mid
    # logo, compare com a parte direita pois ela não vai estar rotacionada, estará ordenada
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (right + left) >> 1
            lower_bound_sorted = nums[left] <= nums[middle]
            target_in_lower_bound = nums[left] <= target <= nums[middle]
            target_in_upper_bound = nums[middle] < target <= nums[right]

            if lower_bound_sorted:
                if target_in_lower_bound:
                    right = middle
                else:
                    left = middle + 1
            else:
                if target_in_upper_bound:
                    left = middle + 1
                else:
                    right = middle
        
        return left if nums[left] == target else -1