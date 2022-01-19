from grid import SudokuGrid
from solver import LogicSolver
from ui import showEntireGrid

problem = [
    [4,0,0,0,0,0,9,3,8],
    [0,3,2,0,9,4,1,0,0],
    [0,9,5,3,0,0,2,4,0],
    [3,7,0,6,0,9,0,0,4],
    [5,2,9,0,0,1,6,7,3],
    [6,0,4,7,0,3,0,9,0],
    [9,5,7,0,0,8,3,0,0],
    [0,0,3,9,0,0,4,0,0],
    [2,4,0,0,3,0,7,0,9]
    ]
 

grid = SudokuGrid(problem)
solver = LogicSolver(grid)
solver.simpleElimination()
showEntireGrid(grid,"This is the grid after simple elimination")
solver.nakedCandidates()
showEntireGrid(grid,"This is the grid after naked Pairs")
for i in range(1):
    solver.hiddenSingles()
    showEntireGrid(grid,"This is the grid after hidden singles, round {}".format(i))