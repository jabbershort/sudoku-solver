from box import SudokuBox
from grid import SudokuGrid
from solver import EliminationSolver, BackTracking
import curses
import time
from examples import exampleGrids
# grid, row column

# grids= [[1,2,3],
#         [4,5,6],
#         [7,8,9]
#         ]

# rows = top row is one, going down
# columns = left is one, going right



if __name__ == "__main__":
    startTime = time.time()
    
    
    print("preparing to initialize screen...")
    screen = curses.initscr()
    print("Screen initialized.")
    screen.refresh()
    

    for grid in exampleGrids:
        if grid == "hard":
            continue
        sudoku = SudokuGrid(exampleGrids[grid]['problem'])
        # solver = EliminationSolver(sudoku,screen)
        solver = BackTracking(sudoku,screen)
        solver.solve()

        if sudoku.getResult() == exampleGrids[grid]['solution']:
            print("The result is correct!")
        else:
            print("The result is incorrect")
    
        if sudoku.completed:
            sudoku.printFinalGrid("Completed in {} seconds with {} cycles required.".format(solver.timeTaken,solver.solveCycle))
            print("The script solved the problem in {} seconds with {} cycles required.".format(solver.timeTaken,solver.solveCycle))
        
        else:
            endTime = time.time()
            sudoku.printFinalGrid("Failed in {} seconds with {} cycles required.".format(solver.timeTaken,solver.solveCycle))
            print("The script failed to solve the problem in {} seconds with {} cycles required.".format(solver.timeTaken,solver.solveCycle))
        
        time.sleep(1)
