class SudokuCell:
    def __init__(self,known: bool,grid: int,column: int,row: int,value: int):
        self.known = known
        self.possibilities = []
        self.grid = grid
        self.column = column
        self.row = row
        self.value = value
        if not self.known:
            self.possibilies = [1,2,3,4,5,6,7,8,9]

    def showPossibilities(self):
        print(self.possibilities)

    def addPossibility(self,value: int):
        if value not in self.possibilities:
            self.possibilities.append(value)

    def removePossibility(self,value: int,initialRun: bool):
        if value in self.possibilities:
            self.possibilities.remove(value)
        if not initialRun and len(self.possibilities) == 1:
            self.value = self.possibilities[0]
            self.known = True


        