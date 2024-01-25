from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def __init__(self) -> None:
        self.rows = 0
        self.columns = 0
        self.wall = -1
        self.empty_room = 2147483647
        self.gate = 0

    def walls_and_gates(self, rooms: list[list[int]]):
        self.rows, self.columns = len( rooms ), len( rooms[0] )

        queue = deque()
        for row in range( self.rows ):
            for column in range( self.columns ):
                if rooms[row][column] == self.gate:
                    queue.append( ( row, column ) )
        
        distance = 1
        while queue:
            rooms_in_level = len( queue )
            for _ in range( rooms_in_level ):
                row, column = queue.popleft()

                self.explore( row - 1, column, rooms, queue, distance )
                self.explore( row + 1, column, rooms, queue, distance )
                self.explore( row, column - 1, rooms, queue, distance )
                self.explore( row, column + 1, rooms, queue, distance )
            
            distance += 1
        
    def explore( self, row, column, rooms, queue, distance ):
        if (
            row < 0 or column < 0 or row >= self.rows or column >= self.columns
            or rooms[row][column] != self.empty_room
        ): return

        rooms[row][column] = distance
        queue.append( ( row, column ) )