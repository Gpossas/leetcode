class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        prerequisites_map = {}
        for course, prerequisite in prerequisites:
            if not course in prerequisites_map:
                prerequisites_map[course] = []
            prerequisites_map[course].append( prerequisite )
        
        visited = set()
        for course in prerequisites_map:
            if self.has_cycle( course, visited, prerequisites_map ):
                return False
        return True
    
    def has_cycle( self, course, visited, prerequisites_map, visiting = set() ) -> bool:
        if course in visited:
            return False
        if course in visiting:
            return True
        
        visiting.add( course )
        for prerequisite in prerequisites_map.get( course, [] ):
            if self.has_cycle( prerequisite, visited, prerequisites_map, visiting ):
                return True
        
        visiting.remove( course )
        visited.add( course )
        return False

print(Solution().canFinish(3, [[0,1],[0,2],[1,2]]))