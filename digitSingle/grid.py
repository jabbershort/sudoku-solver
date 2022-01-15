from cell import SudokuCell

class SudokuGrid:
    def __init__(self,list):
        self.cells = []
        self.numSolved = 0
        self.completed = False
        self.populateGrid(list)
        self.howCompleteAmI()
    
    def populateGrid(self,list):
        for i in range (0,9):
            for j in range(0,9):
                value = list[i][j]
                if value != 0:
                    known = True
                else:
                    known = False
                column = j+1
                row = i+1

                if i < 3:
                    if j <3:
                        grid = 1
                    elif j < 6:
                        grid = 2
                    else:
                        grid = 3
                elif i < 6:
                    if j <3:
                        grid = 4
                    elif j < 6:
                        grid = 5
                    else:
                        grid = 6
                else:
                    if j <3:
                        grid = 7
                    elif j < 6:
                        grid = 8
                    else:
                        grid = 9
                cell = SudokuCell(known,grid,column,row,value)
                self.cells.append(cell)

    def howCompleteAmI(self):
        self.numSolved = 0
        for cell in self.cells:
            if cell.known:
                self.numSolved += 1
        return self.numSolved 

    def checkAllCells(self):
        testSolve = True
        for cell in self.cells:
            if cell.known:
                continue
            else:
                testSolve = False
                if len(cell.possibilities) == 1:
                    cell.value = cell.possibilities[0]
                    cell.known = True
        if testSolve == True:
            self.completed = True

    def fetchValue(self,column,row):
        for cell in self.cells:
            if cell.column == column and cell.row == row:
                if cell.value != 0:
                    return cell.value
                else:
                    return "?"
        return "?"

    def analyseCells(self):
        for cell in (cell for cell in self.cells if cell.known == False):
            self.analyseCell(cell)
        for i in range(1,10):
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
            for cell2 in (cell2 for cell2 in self.cells if cell2.known == False):
                if cell.id == cell2.id:
                    continue
                if cell2.column == cell.column or cell.row == cell2.row or cell.grid == cell2.grid:
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
        for cell in (cell for cell in self.cells if cell.row == row and cell.known == False):
            for pos in cell.possibilities:
                opt.append(pos)
        opt.sort()

        for i in range(1,10):
            if opt.count(i) == 1:
                for cell in (cell for cell in self.cells if cell.row == row and cell.known == False):
                    if i in cell.possibilities:
                        cell.known = True
                        cell.value = i
        
    def analyseCol(self,col):
        opt = []
        for cell in (cell for cell in self.cells if cell.column == col and cell.known == False):
            for pos in cell.possibilities:
                opt.append(pos)
        opt.sort()

        for i in range(1,10):
            if opt.count(i) == 1:
                for cell in (cell for cell in self.cells if cell.column == col and cell.known == False):
                    if i in cell.possibilities:
                        cell.known = True
                        cell.value = i

    def analyseGrid(self,grid):
        opt = []
        for cell in (cell for cell in self.cells if cell.grid == grid and cell.known == False):
            for pos in cell.possibilities:
                opt.append(pos)
        opt.sort()
        for i in range(1,10):
            if opt.count(i) == 1:
                for cell in (cell for cell in self.cells if cell.grid == grid and cell.known == False):
                    if i in cell.possibilities:
                        cell.known = True
                        cell.value = i 


    def updateOption(self,cell):
        for cell2 in self.cells:
            if cell == cell2:
                    continue
            if cell.grid == cell2.grid or cell.column == cell2.column or cell.row == cell2.row:
                if cell2.known:
                    cell.removePossibility(cell2.value)
            else:
                continue

    def updateOptions(self):
        for cell in (cell for cell in self.cells if cell.known == False):
            self.updateOption(cell)
        self.checkAllCells()

    def showCurrentGrid(self,screen,message = ""):
        screen.clear()
        for i in range(1,4):
            screen.addstr(i,0,"{} {} {} | {} {} {} | {} {} {}"
                .format(self.fetchValue(1,i),self.fetchValue(2,i),self.fetchValue(3,i),self.fetchValue(4,i),self.fetchValue(5,i),self.fetchValue(6,i),self.fetchValue(7,i),self.fetchValue(8,i),self.fetchValue(9,i)))

        screen.addstr(4,0," - - -   - - -   - - -")

        for i in range(4,8):
            screen.addstr(i+1,0,"{} {} {} | {} {} {} | {} {} {}"
                .format(self.fetchValue(1,i),self.fetchValue(2,i),self.fetchValue(3,i),self.fetchValue(4,i),self.fetchValue(5,i),self.fetchValue(6,i),self.fetchValue(7,i),self.fetchValue(8,i),self.fetchValue(9,i)))

        screen.addstr(8,0," - - -   - - -   - - -")

        for i in range(7,10):
            screen.addstr(i+2,0,"{} {} {} | {} {} {} | {} {} {}"
                .format(self.fetchValue(1,i),self.fetchValue(2,i),self.fetchValue(3,i),self.fetchValue(4,i),self.fetchValue(5,i),self.fetchValue(6,i),self.fetchValue(7,i),self.fetchValue(8,i),self.fetchValue(9,i)))
        if message != "":
            screen.addstr(12,0,message)
        screen.refresh()

    def printFinalGrid(self):
        for i in range(1,4):
            print("{} {} {} | {} {} {} | {} {} {}"
                .format(self.fetchValue(1,i),self.fetchValue(2,i),self.fetchValue(3,i),self.fetchValue(4,i),self.fetchValue(5,i),self.fetchValue(6,i),self.fetchValue(7,i),self.fetchValue(8,i),self.fetchValue(9,i)))

        print(" - - -   - - -   - - -")

        for i in range(4,7):
            print("{} {} {} | {} {} {} | {} {} {}"
                .format(self.fetchValue(1,i),self.fetchValue(2,i),self.fetchValue(3,i),self.fetchValue(4,i),self.fetchValue(5,i),self.fetchValue(6,i),self.fetchValue(7,i),self.fetchValue(8,i),self.fetchValue(9,i)))

        print(" - - -   - - -   - - -")

        for i in range(7,10):
            print("{} {} {} | {} {} {} | {} {} {}"
                .format(self.fetchValue(1,i),self.fetchValue(2,i),self.fetchValue(3,i),self.fetchValue(4,i),self.fetchValue(5,i),self.fetchValue(6,i),self.fetchValue(7,i),self.fetchValue(8,i),self.fetchValue(9,i)))
