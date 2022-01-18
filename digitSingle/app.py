from box import SudokuBox
from grid import SudokuGrid
from solver import EliminationSolver, LogicSolver, BackTracking
import curses
import time
import json
import random


# grid, row column

# grids= [[1,2,3],
#         [4,5,6],
#         [7,8,9]
#         ]

# rows = top row is one, going down
# columns = left is one, going right

def loadExamples(num):
    with open("E:\devops\sudoku-solver\generate\puzzles\puzzles.json") as f:
        data = json.load(f)
    puzzleNames = list(data.keys())
    examples = {}
    for i in range(num):
        name = random.choice(puzzleNames)
        examples[name] = data[name]
    return examples

def printCompletion(sudoku: SudokuGrid,solver,screen):
    if sudoku.completed:
        if sudoku.getResult() == examples[grid]['solution']:
            solution = "correctly"
        else:
            solution ="incorrectly"
        sudoku.showCurrentGrid(screen,"Completed {} in {} seconds.".format(solution,solver.timeTaken))
        print("The script solved the {} problem {} {} in {} seconds.".format(examples[grid]['difficulty'],grid,solution,solver.timeTaken))
        curses.napms(5000)

    else:
        sudoku.showCurrentGrid(screen,"Failed in {} seconds.".format(solver.timeTaken))
        print("The script failed to solve the {} problem {} in {} seconds.".format(examples[grid]['difficulty'],grid,solver.timeTaken))
        curses.napms(5000)


if __name__ == "__main__":    
    print("preparing to initialize screen...")
    screen = curses.initscr()
    print("Screen initialized.")
    screen.refresh()
    # screen = ""
    
    examples = loadExamples(10)

    # print(examples)
    for grid in examples:
        print("Attempting to solve {} problem: {}.".format(examples[grid]['difficulty'],grid))
        sudoku = SudokuGrid(examples[grid]['problem'])
        
        #Elimination First
        solver = LogicSolver(sudoku,screen)
        solver.solve()

        if sudoku.completed:
            printCompletion(sudoku,solver,screen)
            continue
        
        print("Failed to find solution!")
