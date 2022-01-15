import curses,time

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

hardest_sudoku = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]]
\
startTime= time.time()
screen = curses.initscr()
screen.refresh()

def getPCCompletion(grid):
    passedNums = 0
    for line in grid:
        for item in (item for item in line if item != 0):
            passedNums +=1
    return round(passedNums/(9*9),2)

def findNextCellToFill(grid, i, j):
    printSolution(grid,time.time()-startTime,getPCCompletion(grid))
    for x in range(i,9):
            for y in range(j,9):
                    if grid[x][y] == 0:
                            return x,y
    for x in range(0,9):
            for y in range(0,9):
                    if grid[x][y] == 0:
                            return x,y
    return -1,-1

def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False


def printSolution(grid,time,pc):
    try:
        screen.clear()
        for i in range(0,3):
            screen.addstr(i,0,"{} {} {} | {} {} {} | {} {} {}".format(grid[i][0],grid[i][1],grid[i][2],grid[i][3],grid[i][4],grid[i][5],grid[i][6],grid[i][7],grid[i][8]))

        screen.addstr(3,0,"- - -   - - -   - - -")

        for i in range(3,6):
            screen.addstr(i+1,0,"{} {} {} | {} {} {} | {} {} {}".format(grid[i][0],grid[i][1],grid[i][2],grid[i][3],grid[i][4],grid[i][5],grid[i][6],grid[i][7],grid[i][8]))

        screen.addstr(7,0,"- - -   - - -   - - -")
        for i in range(6,9):
            screen.addstr(i+2,0,"{} {} {} | {} {} {} | {} {} {}".format(grid[i][0],grid[i][1],grid[i][2],grid[i][3],grid[i][4],grid[i][5],grid[i][6],grid[i][7],grid[i][8]))
        
        screen.addstr(11,0,"The current percentage completion is {}.".format(pc))
        screen.addstr(12,0,"It has taken {} seconds.".format(round(time,3)))
        screen.refresh()
    except:
        print("Print failure")

def printSolution2(grid):
    try:
        for i in range(0,3):
            print("{} {} {} | {} {} {} | {} {} {}".format(grid[i][0],grid[i][1],grid[i][2],grid[i][3],grid[i][4],grid[i][5],grid[i][6],grid[i][7],grid[i][8]))

        print("- - -   - - -   - - -")

        for i in range(3,6):
            print("{} {} {} | {} {} {} | {} {} {}".format(grid[i][0],grid[i][1],grid[i][2],grid[i][3],grid[i][4],grid[i][5],grid[i][6],grid[i][7],grid[i][8]))

        print("- - -   - - -   - - -")
        for i in range(6,9):
            print("{} {} {} | {} {} {} | {} {} {}".format(grid[i][0],grid[i][1],grid[i][2],grid[i][3],grid[i][4],grid[i][5],grid[i][6],grid[i][7],grid[i][8]))
    except:
        print("Print failure")


solveSudoku(gridHARD)
endTime= time.time()
print("finish time {}".format(endTime-startTime))
