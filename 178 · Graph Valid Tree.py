class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def __init__(self) -> None:
        self.parents = None
        self.rank = None

    def valid_tree(self, n: int, edges: list[list[int]]) -> bool:
        # to be a tree must be n - 1 edges and don't have a cycle

        self.parents = [node for node in range(n)]
        self.rank = [1] * n

        if len(edges) != n - 1:
            return False
        
        for edge in edges:
            if self.has_cycle(*edge):
                return False
        return True
        
    def find(self, num):
        if num == self.parents[num]:
            return num
        self.parents[num] = self.find(self.parents[num])
        return self.parents[num]
    
    def has_cycle(self, set1, set2) -> bool:
        smaller = self.find(set1)
        bigger = self.find(set2)

        # has a cycle
        if smaller == bigger:
            return True
        
        if self.rank[smaller] > self.rank[bigger]:
            smaller, bigger = bigger, smaller

        self.parents[smaller] = bigger
        if self.rank[smaller] == self.rank[bigger]:
            self.rank[bigger] += 1
        return False

    def valid_tree_DFS(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        # create graph representation
        adjacency_list = {}
        for node1, node2 in edges:
            if not node1 in adjacency_list:
                adjacency_list[node1] = []
            if not node2 in adjacency_list:
                adjacency_list[node2] = []

            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)
        
        visited = set()
        return (
            not self.has_cycle_dfs(0, -1, visited, adjacency_list)
            and n == len(visited) # if false graph is disconnected
        )

    def has_cycle_dfs(self, node, parent, visited, adjacency_list):
        if node in visited:
            return True
        
        visited.add(node)
        for neighbor in adjacency_list.get(node, []):
            if neighbor == parent:
                continue
            if self.has_cycle_dfs( neighbor, node, visited, adjacency_list ):
                return True
        return False
    
r = Solution().valid_tree_DFS(10, [[0,1],[5,6],[6,7],[9,0],[3,7],[4,8],[1,8],[5,2],[5,3]])
print(r)