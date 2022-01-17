import json,copy
fileName = "/data/puzzles.json"


def getDictionary():
    f = open(fileName)
    dataIn = json.load(f)
    return dataIn

def addSolutionToDict(name,solution):
    f = open(fileName)
    dataIn = json.load(f)
    dataIn[name]['solution'] = solution
    with open(fileName,"w") as fb:
        json.dump(dataIn,fb)


def iterativeSolve(dict):
    for key in dict:
        print("Finding solution to problem {}, which is a {} difficulty.".format(key,dict[key]['difficulty']))
        solution = copy.copy(dict[key]['problem'])
        solveSudoku(solution)
        addSolutionToDict(key,solution)


def findNextCellToFill(grid, i, j):
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

def findSolutions():
    iterativeSolve(getDictionary())

if __name__ == "__main__":
    findSolutions()