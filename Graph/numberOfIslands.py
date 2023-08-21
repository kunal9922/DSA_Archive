'''Number of islands'''
def markIsland(grid: list,rowIdx, colIdx, rows, cols):
    #base case for out of bound indexes
    if (rowIdx < 0) or (colIdx < 0) or (rowIdx >= rows) or (colIdx >= cols):
        return
    elif grid[rowIdx][colIdx] in [0, 2]: # Water is not visitable or visiting visited land again
        return
    # marking land visited as 2
    else: # land 
        grid[rowIdx][colIdx] = 2
        #making recursive call to marking as visited
        markIsland(grid, rowIdx, colIdx - 1, rows, cols) # for left direction
        markIsland(grid, rowIdx, colIdx + 1, rows, cols) # for rigth direction
        markIsland(grid, rowIdx - 1, colIdx, rows, cols) # for up direction
        markIsland(grid, rowIdx + 1, colIdx, rows, cols) # for down direction



def numIslands(grid: list) -> int:
    rows = len(grid)
    if rows == 0: # Empty grid boundary case
        return 0
    cols = len(grid[0])

    noOfislands = 0 
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1: # We have found an Island
                markIsland(grid, row, col, rows, cols)
                noOfislands += 1
    
    return noOfislands

grid = [
    [0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1],
]
print(numIslands(grid))