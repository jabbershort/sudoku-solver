class SudokuCell:
    def __init__(self,known: bool,grid: int,column: int,row: int,value: int):
        self.known = known
        self.possibilities = []
        self.grid = grid
        self.column = column
        self.row = row
        self.value = value
        self.id = "{}-{}-{}".format(grid,row,column)
        if not self.known:
            self.possibilities = [1,2,3,4,5,6,7,8,9]

    def showPossibilities(self):
        print(self.possibilities)

    def addPossibility(self,value: int):
        if value not in self.possibilities:
            self.possibilities.append(value)

    def removePossibility(self,value: int):
        if value in self.possibilities:
            self.possibilities.remove(value)
        if len(self.possibilities) == 1:
            self.known = True
            self.value = self.possibilities[0]


        