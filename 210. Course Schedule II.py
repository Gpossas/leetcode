class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        prerequisites_map = {}
        for course, prerequisite in prerequisites:
            if not course in prerequisites_map:
                prerequisites_map[course] = []
            prerequisites_map[course].append( prerequisite )
        
        visited = set()
        result = []
        for course in range( numCourses ):
            if self.has_cycle( course, result, prerequisites_map, visited, visiting=set() ):
                return []
        return result
    
    def has_cycle( self, course, result, prerequisites_map, visited, visiting ):
        if course in visited:
            return False
        if course in visiting:
            return True
        
        visiting.add( course )
        for prerequisite in prerequisites_map.get( course, [] ):
            if self.has_cycle( prerequisite, result, prerequisites_map, visited, visiting ):
                return True
        
        visiting.remove( course )
        visited.add( course )
        result.append( course )
        return False