from sys import settrace


class SudokuBox:
    def __init__(self,known: bool,box: int,column: int,row: int,value: int):
        self.known = known
        self.options = []
        self.box = box
        self.column = column
        self.row = row
        self.value = value
        self.id = "{}-{}-{}".format(box,row,column)
        if not self.known:
            self.options = [1,2,3,4,5,6,7,8,9]
        else:
            self.options = [value]

    def setValue(self,newValue):
        self.value = newValue
        self.options = [newValue]
        self.known = True
        return True


    def checkCell(self):
        if len(self.options) == 1:
            self.setValue(self.options[0])
            return True
        else:
            return False


    def showPossibilities(self):
        print(self.possibilities)

    def addPossibility(self,value: int):
        if value not in self.possibilities:
            self.possibilities.append(value)
            return True
        else:
            return False

    def removePossibility(self,value: int):
        if value in self.options:
            if len(self.options) <= 1:
                return False
            else:
                self.options.remove(value)
                return True
        if len(self.options) == 1:
            self.value = self.options[0]
            self.known = True
            return True


    
        