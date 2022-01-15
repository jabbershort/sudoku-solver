from cell import SudokuCell
from grid import SudokuGrid
import curses
import time
# grid, row column

# grids= [[1,2,3],
#         [4,5,6],
#         [7,8,9]
#         ]

# rows = top row is one, going down
# columns = left is one, going right

gridEASY = [
    [0,0,4,0,5,0,0,0,0],
    [9,0,0,7,3,4,6,0,0],
    [0,0,3,0,2,1,0,4,9],
    [0,3,5,0,9,0,4,8,0],
    [0,9,0,0,0,0,0,3,0],
    [0,7,6,0,1,0,9,2,0],
    [3,1,0,9,7,0,2,0,0],
    [0,0,9,1,8,2,0,0,3],
    [0,0,0,0,6,0,1,0,0]
]

gridHARD = [
    [0,0,0,0,0,0,5,4,0],
    [7,0,0,3,0,0,0,0,9],
    [0,0,5,8,0,0,0,7,0],
    [0,0,0,0,0,0,0,0,0],
    [0,2,0,0,8,0,0,0,7],
    [9,0,0,6,0,0,0,0,1],
    [0,0,9,0,2,0,1,0,4],
    [5,0,0,0,4,0,0,0,0],
    [6,0,0,0,1,0,0,0,8]
    ]


if __name__ == "__main__":
    startTime = time.time()
    
    
    print("preparing to initialize screen...")
    screen = curses.initscr()
    print("Screen initialized.")
    screen.refresh()
    
    game = SudokuGrid(gridHARD)
    game.showCurrentGrid(screen,"Initial Operation")
    
    count = 1
    cycleLimit = 1000
    previousPC = 0
    completionPC = 0


    while not game.completed:
        if count > cycleLimit:
            break
        game.analyseCells()
        previousPC = completionPC
        completionPC = round((game.howCompleteAmI()/(9*9))*100,1)
        # if not completionPC > previousPC:
        #     break
        game.showCurrentGrid(screen,"Updating options, round {}, {}% complete.".format(count,completionPC))
        count += 1
    
    if game.completed:
        endTime = time.time()
        game.showCurrentGrid(screen,"Completed in {} seconds with {} cycles required.".format(round(endTime-startTime,4),count))
        print("The script solved the problem in {} seconds with {} cycles required.".format(round(endTime-startTime,4),count))
    
    else:
        endTime = time.time()
        game.showCurrentGrid(screen, "Failed in {} seconds with {} cycles required.".format(round(endTime-startTime,4),count))
        print("The script failed to solve the problem in {} seconds with {} cycles required.".format(round(endTime-startTime,4),count))

    # curses.napms(5000)

    game.printFinalGrid()

