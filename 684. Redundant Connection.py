class Solution:
    def __init__(self) -> None:
        self.parents = None
        self.rank = None
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # edges 1 indexed
        self.parents = [num for num in range(len(edges) + 1)]
        self.rank = [0 for _ in range(len(self.parents))]

        for edge in edges:
            if self.union(*edge):
                return edge
    
    def find(self, num) -> int:
        if self.parents[num] == num:
            return num
        self.parents[num] = self.find(self.parents[num])
        return self.parents[num]
    
    def union(self, set1, set2) -> bool:
        smaller = self.find(set1)
        bigger = self.find(set2)

        if smaller == bigger:
            return True
        
        if self.rank[smaller] > self.rank[bigger]:
            smaller, bigger = bigger, smaller

        # merge small tree into the bigger tree
        # change the representative of the smaller set to the bigger set
        self.parents[smaller] = bigger
        if self.rank[smaller] == self.rank[bigger]:
            self.rank[bigger] += 1
        return False