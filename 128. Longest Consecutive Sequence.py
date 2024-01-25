class Solution:
    def __init__(self) -> None:
        self.representatives = {}
        self.size = {}
    def longestConsecutive(self, nums: list[int]) -> int:
        max_size = 0

        for num in nums:
            # only calculate non repeated nums
            if num not in self.representatives:
                group_size = 1
                self.representatives[num] = num
                self.size[num] = group_size

                if num - 1 in self.representatives:
                    group_size = self.union(num - 1, num)
                if num + 1 in self.representatives:
                    group_size = self.union(num, num + 1)

                max_size = max(max_size, group_size)
        return max_size
    
    def find(self, num):
        if self.representatives[num] == num:
            return num
        
        self.representatives[num] = self.find(self.representatives[num])
        return self.representatives[num]

    def union(self, set1, set2):
        smaller = self.find(set1)
        bigger = self.find(set2)

        if smaller == bigger:
            return 0
        
        if self.size[smaller] > self.size[bigger]:
            smaller, bigger = bigger, smaller

        self.representatives[smaller] = bigger
        self.size[bigger] += self.size[smaller]

        return self.size[bigger]