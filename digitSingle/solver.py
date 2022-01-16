from grid import SudokuGrid
from box import SudokuBox
import time, curses

class EliminationSolver:
    def __init__(self,grid: SudokuGrid,screen=""):
        self.grid = grid
        self.screen = screen
        self.solveCycle = 0

    def solve(self,cycleLimit = 1000):
        self.cycleLimit = cycleLimit
        self.startTime = time.time()
        while not self.grid.completed:
            if self.solveCycle > self.cycleLimit:
                break
            else:
                self.analyseCells()
                completionPC = round((self.grid.howCompleteAmI()/(9*9))*100,1)
                if self.screen != "":
                    self.grid.showCurrentGrid(self.screen,"Updating options, round {}, {}% complete.".format(self.solveCycle,completionPC))
                self.solveCycle += 1

        self.endTime = time.time()
        self.timeTaken = round(self.endTime - self.startTime,4)


    def updateOption(self,cell):
        for cell2 in self.grid.cells:
            if cell == cell2:
                    continue
            if cell.box == cell2.box or cell.column == cell2.column or cell.row == cell2.row:
                if cell2.known:
                    cell.removePossibility(cell2.value)
            else:
                continue

    def updateOptions(self):
        for cell in (cell for cell in self.cells if cell.known == False):
            self.updateOption(cell)
        self.checkAllCells()

    def analyseCells(self):
        for cell in (cell for cell in self.grid.cells if cell.known == False):
            self.analyseCell(cell)
        for i in range(0,9):
            self.analyseGrid(i)
            self.analyseCol(i)
            self.analyseRow(i)
        self.checkAllCells()
    
    def analyseCell(self,cell):
        if cell.known:
            return
        else:
            otherPoss = []
            self.updateOption(cell)
            for cell2 in (cell2 for cell2 in self.grid.cells if cell2.known == False):
                if cell.id == cell2.id:
                    continue
                if cell2.column == cell.column or cell.row == cell2.row or cell.box == cell2.box:
                    for poss in cell2.possibilities:
                        otherPoss.append(poss)
            
            otherPoss.sort()
            for poss in cell.possibilities:
                if poss in otherPoss:
                    continue
                else:
                    cell.known = True
                    cell.value = poss
                    return



    def analyseRow(self,row):
        opt = []
        for cell in (cell for cell in self.grid.cells if cell.row == row and cell.known == False):
            for pos in cell.possibilities:
                opt.append(pos)
        opt.sort()

        for i in range(0,9):
            if opt.count(i) == 1:
                for cell in (cell for cell in self.grid.cells if cell.row == row and cell.known == False):
                    if i in cell.possibilities:
                        cell.known = True
                        cell.value = i
        
    def analyseCol(self,col):
        opt = []
        for cell in (cell for cell in self.grid.cells if cell.column == col and cell.known == False):
            for pos in cell.possibilities:
                opt.append(pos)
        opt.sort()

        for i in range(0,9):
            if opt.count(i) == 1:
                for cell in (cell for cell in self.grid.cells if cell.column == col and cell.known == False):
                    if i in cell.possibilities:
                        cell.known = True
                        cell.value = i

    def analyseGrid(self,box):
        opt = []
        for cell in (cell for cell in self.grid.cells if cell.box == box and cell.known == False):
            for pos in cell.possibilities:
                opt.append(pos)
        opt.sort()
        for i in range(0,9):
            if opt.count(i) == 1:
                for cell in (cell for cell in self.grid.cells if cell.box == box and cell.known == False):
                    if i in cell.possibilities:
                        cell.known = True
                        cell.value = i 

    def checkAllCells(self):
        testSolve = True
        for cell in self.grid.cells:
            if cell.known:
                continue
            else:
                testSolve = False
                if len(cell.possibilities) == 1:
                    cell.value = cell.possibilities[0]
                    cell.known = True
        if testSolve == True:
            self.grid.completed = True

class BackTracking:
    def __init__(self,grid:SudokuGrid,screen):
        self.grid = grid
        self.screen = screen
        self.solveCycle = 0

    def solve(self):
        self.startTime = time.time()

        self.solveSudoku()

        self.endTime = time.time()
        self.timeTaken = round(self.endTime - self.startTime,4)


    def findNextCellToFill(self,i, j):
        self.grid.showCurrentGrid(self.screen)
        for x in range(i,9):
                for y in range(j,9):
                        if self.grid.getValue(x,y) == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if self.grid.getValue(x,y,) == 0:
                                return x,y
        return -1,-1  

    def isValid(self,i, j, e):
        rowOk = all([e != self.grid.getValue(i,x) for x in range(9)])
        if rowOk:
                columnOk = all([e != self.grid.getValue(x,j) for x in range(9)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if self.grid.getValue(x,y) == e:
                                                return False
                        return True
        return False

    def solveSudoku(self,i=0, j=0):
        self.solveCycle +=1
        i,j = self.findNextCellToFill(i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if self.isValid(i,j,e):
                    self.grid.setValue(i,j,e)
                    if self.solveSudoku(i, j):
                        return True
                    # Undo the current cell for backtracking
                    self.grid.setValue(i,j,0)
        return False