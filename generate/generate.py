from dataclasses import replace
import subprocess, random, json

difficulties = ['simple','easy','intermediate','expert']

def saveFile(seed,puzzle,solution,difficulty):
    dict = {
        'difficulty': diff,
        'problem': puzzle,
        'solution': solution
    }
    fileName = "/data/"+difficulty+"-"+str(seed)+".json"
    with open(fileName,'w') as fp:
        json.dump(dict,fp)


def generatePuzzle(difficulty):
    command = "qqwing --generate --difficulty "+difficulty+" --compact"
    puzzle = subprocess.check_output(command.split())
    puzzleList = convertPuzzle(puzzle)
    return puzzleList    
    #return convertPuzzle(puzzleList)

def convertPuzzle(puzzleStringIn):
    replacedString = []
    for char in puzzleStringIn:
        if chr(char) == "\n":
            continue
        if char == 46:
            replacedString.append(0)
        else:
            replacedString.append(int(chr(char)))
    
    # return replacedString
    return(rowReduction(replacedString))

def rowReduction(lst):
    puzzle = []
    puzzle.append(lst[0:9])
    puzzle.append(lst[9:18])
    puzzle.append(lst[18:27])
    puzzle.append(lst[27:36])
    puzzle.append(lst[36:45])
    puzzle.append(lst[45:54])
    puzzle.append(lst[54:63])
    puzzle.append(lst[63:72])
    puzzle.append(lst[72:81])
    return puzzle

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


if __name__ == "__main__":
    for i in range(0,10):
        seed = random.randint(1,1000000)
        diff = random.choice(difficulties)
        puzzle = generatePuzzle(diff)
        solution = puzzle.copy()
        solveSudoku(solution)
        saveFile(seed,puzzle,solution,diff)
    

