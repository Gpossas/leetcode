from collections import deque

class Solution:
    def __init__(self) -> None:
        self.rows = 0
        self.columns = 0
        self.ROTTEN = 2
    def orangesRotting(self, grid: list[list[int]]) -> int:
        self.rows, self.columns = len( grid ), len( grid[0] )
        count = { 'fresh_oranges': 0 }
        rotten = deque()

        # Precomputaion: get num of fresh oranges and put rotten oranges in rotten
        for row in range( self.rows ):
            for column in range( self.columns ):
                if grid[row][column] == 1:
                    count['fresh_oranges'] += 1
                elif grid[row][column] == 2:
                    rotten.append( ( row, column ) )
        
        minutes = 0
        while rotten and count['fresh_oranges'] > 0:
            nodes_in_level = len( rotten )
            for _ in range( nodes_in_level ):
                row, column = rotten.popleft()

                self.explore( row - 1, column, grid, rotten, count )
                self.explore( row + 1, column, grid, rotten, count )
                self.explore( row, column - 1, grid, rotten, count )
                self.explore( row, column + 1, grid, rotten, count )
            
            minutes += 1
        
        return minutes if count['fresh_oranges'] == 0 else -1

    def explore( self, row, column, grid, rotten, count ):
        if ( 
            row >= self.rows or column >= self.columns or row < 0 or column < 0 
            or grid[row][column] != 1
        ): return

        grid[row][column] = self.ROTTEN
        rotten.append( ( row, column ) ) 
        count['fresh_oranges'] -= 1