from cell import SudokuCell

class SudokuGrid:
    def __init__(self,list):
        self.cells = []
        self.numSolved = 0
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

    def checkSingleOptions(self):
        for cell in self.cells:
            if len(cell.possibilities) == 1:
                cell.value = cell.possibilites[0]
                cell.known = True

    def updateCellOptions(self):
        for i in range(1,10):
            knownValues = []
            for cell in self.cells:
                if cell.grid == i:
                    if cell.known:
                        knownValues.append(cell.value)
            possibleValues = [1,2,3,4,5,6,7,8,9]
            for val in knownValues:
                possibleValues.remove(val)
            for cell in self.cells:
                if cell.grid == i:
                    for val in possibleValues:
                        if val not in cell.possibilites:
                            cell.possibilites.append(val)

    def updateColumnOptions(self):
        for i in range(1,10):
            knownValues = []
            for cell in self.cells:
                if cell.column == i:
                    if cell.known:
                        knownValues.append(cell.value)
            possibleValues = [1,2,3,4,5,6,7,8,9]
            for val in knownValues:
                possibleValues.remove(val)
            for cell in self.cells:
                if cell.column == i:
                    for val in possibleValues:
                        if val not in cell.possibilites:
                            cell.possibilites.append(val)
    
    def updateRowOptions(self):
        for i in range(1,10):
            knownValues = []
            for cell in self.cells:
                if cell.row == i:
                    if cell.known:
                        knownValues.append(cell.value)
            possibleValues = [1,2,3,4,5,6,7,8,9]
            for val in knownValues:
                possibleValues.remove(val)
            for cell in self.cells:
                if cell.row == i:
                    for val in possibleValues:
                        if val not in cell.possibilites:
                            cell.possibilites.append(val)
                
