from cell import SudokuCell
from grid import SudokuGrid

# grid, row column

# grids= [[1,2,3],
#         [4,5,6],
#         [7,8,9]
#         ]

# rows = top row is one, going down
# columns = left is one, going right

grid = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
    ]

game = SudokuGrid(grid)

game.updateCellPossibilities()

print(game.cells[0].possibilities)
        