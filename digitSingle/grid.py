from box import SudokuBox

class SudokuGrid:
    def __init__(self,list):
        self.cells = []
        self.numSolved = 0
        self.completed = False
        self.populateGrid(list)
        self.updatePossibilities()
        self.howCompleteAmI()

    def updatePossibilities(self):
        for cell in self.cells:
            if cell.known:
                continue
            else:
                for cell2 in (cell2 for cell2 in self.cells if cell2.known == True and cell.id != cell2.id):
                    if cell2.row == cell.row or cell2.column == cell.column or cell2.box == cell.box:
                        cell.removePossibility(cell2.value)

                # print("Cell {} has possibilities {}.".format(cell.id,cell.options))
        for cell in self.cells:
            cell.checkCell()

    def populateGrid(self,list):
        for i in range (0,9):
            for j in range(0,9):
                value = list[i][j]
                if value != 0:
                    known = True
                else:
                    known = False
                column = j
                row = i

                if i < 3:
                    if j <3:
                        grid = 0
                    elif j < 6:
                        grid = 1
                    else:
                        grid = 2
                elif i < 6:
                    if j <3:
                        grid = 3
                    elif j < 6:
                        grid = 4
                    else:
                        grid = 5
                else:
                    if j <3:
                        grid = 6
                    elif j < 6:
                        grid = 7
                    else:
                        grid = 8
                cell = SudokuBox(known,grid,column,row,value)
                self.cells.append(cell)

    def howCompleteAmI(self):
        self.numSolved = 0
        for cell in self.cells:
            if cell.known:
                self.numSolved += 1
        return self.numSolved 

    def removePossibilityBox(self,box,num,cellIds):
        for cell in (cell for cell in self.cells if cell.box == box and cell.id not in cellIds):
            cell.removePossibility(num)        

    def fetchValue(self,column,row):
        for cell in self.cells:
            if cell.column == column and cell.row == row:
                if cell.value != 0:
                    return cell.value
                else:
                    return "?"
        return "?"
    
    def getPossibilitiesRow(self,row):
        poss = []
        for cell in (cell for cell in self.cells if cell.row == row and cell.known == False):
            for cellPoss in cell.options:
                poss.append(cellPoss)
        return poss
    
    def getPossibilitiesColumn(self,column):
        poss = []
        for cell in (cell for cell in self.cells if cell.column == column and cell.known == False):
            for cellPoss in cell.options:
                poss.append(cellPoss)
        return poss   

    def getPossibilitiesBox(self,box):
        poss = []
        for cell in (cell for cell in self.cells if cell.box == box and cell.known == False):
            for cellPoss in cell.options:
                poss.append(cellPoss)
        return poss   

    def getValue(self,row,column):
        for cell in self.cells:
            if cell.column == column and cell.row == row:
                return cell.value
    
    def getResult(self):
        result = []
        for i in range(0,9):
            row = []
            for j in range(0,9):
                for cell in self.cells:
                    if cell.row == i and cell.column == j:
                        row.append(cell.value)
            result.append(row)
        return result

    def getCell(self,row,column):
        for cell in (cell for cell in self.cells if cell.column == column and cell.row == row):
            return cell


    def showCurrentGrid(self,screen,message = ""):
        if screen == "":
            return
        screen.clear()
        for i in range(0,3):
            screen.addstr(i+1,0,"{} {} {} | {} {} {} | {} {} {}"
                .format(self.fetchValue(0,i),self.fetchValue(1,i),self.fetchValue(2,i),self.fetchValue(3,i),self.fetchValue(4,i),self.fetchValue(5,i),self.fetchValue(6,i),self.fetchValue(7,i),self.fetchValue(8,i)))

        screen.addstr(4,0," - - -   - - -   - - -")

        for i in range(3,7):
            screen.addstr(i+2,0,"{} {} {} | {} {} {} | {} {} {}"
                .format(self.fetchValue(0,i),self.fetchValue(1,i),self.fetchValue(2,i),self.fetchValue(3,i),self.fetchValue(4,i),self.fetchValue(5,i),self.fetchValue(6,i),self.fetchValue(7,i),self.fetchValue(8,i)))

        screen.addstr(8,0," - - -   - - -   - - -")

        for i in range(6,9):
            screen.addstr(i+3,0,"{} {} {} | {} {} {} | {} {} {}"
                .format(self.fetchValue(0,i),self.fetchValue(1,i),self.fetchValue(2,i),self.fetchValue(3,i),self.fetchValue(4,i),self.fetchValue(5,i),self.fetchValue(6,i),self.fetchValue(7,i),self.fetchValue(8,i)))
        if message != "":
            screen.addstr(12,0,message)
        screen.refresh()

    def printFinalGrid(self,message=""):
        for i in range(0,3):
            print("{} {} {} | {} {} {} | {} {} {}"
                .format(self.fetchValue(0,i),self.fetchValue(1,i),self.fetchValue(2,i),self.fetchValue(3,i),self.fetchValue(4,i),self.fetchValue(5,i),self.fetchValue(6,i),self.fetchValue(7,i),self.fetchValue(8,i)))

        print(" - - -   - - -   - - -")

        for i in range(3,6):
            print("{} {} {} | {} {} {} | {} {} {}"
                .format(self.fetchValue(0,i),self.fetchValue(1,i),self.fetchValue(2,i),self.fetchValue(3,i),self.fetchValue(4,i),self.fetchValue(5,i),self.fetchValue(6,i),self.fetchValue(7,i),self.fetchValue(8,i)))

        print(" - - -   - - -   - - -")

        for i in range(6,9):
            print("{} {} {} | {} {} {} | {} {} {}"
                .format(self.fetchValue(0,i),self.fetchValue(1,i),self.fetchValue(2,i),self.fetchValue(3,i),self.fetchValue(4,i),self.fetchValue(5,i),self.fetchValue(6,i),self.fetchValue(7,i),self.fetchValue(8,i)))
        print(message)