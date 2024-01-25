class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def __init__(self) -> None:
        self.parents = None
        self.rank = None

    def count_components(self, n: int, edges: list[list[int]]) -> int:
        self.parents = [num for num in range(n)]
        self.rank = [1 for _ in range(n)]

        for edge in edges:
            n -= self.union(*edge)
        return n
    
    def find(self, num):
        if num == self.parents[num]:
            return num
        self.parents[num] = self.find(self.parents[num])
        return self.parents[num]
    
    def union(self, set1: int, set2: int):
        smaller = self.find(set1)
        bigger = self.find(set2)

        if smaller == bigger:
            return 0
        
        if self.rank[smaller] > self.rank[bigger]:
            smaller, bigger = bigger, smaller
        
        self.parents[smaller] = bigger
        if self.rank[smaller] == self.rank[bigger]:
            self.rank[bigger] += 1
        return 1