from sys import settrace


class SudokuBox:
    def __init__(self,known: bool,box: int,column: int,row: int,value: int):
        self._known = known
        self.possibilities = []
        self.box = box
        self.column = column
        self.row = row
        self._value = value
        self.id = "{}-{}-{}".format(box,row,column)
        if not self.known:
            self.options = [1,2,3,4,5,6,7,8,9]
        else:
            self.options = [value]

    @property
    def value(self):
        return self._value

    @property
    def known(self):
        return self._known

    @value.setter
    def value(self,newValue):
        self._value = newValue
        self.options = [newValue]
        self._known = True
        return True


    def checkCell(self):
        if len(self.options) == 1:
            self.value(self.options[0])
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
            self._value = self.options[0]
            self._known = True
            return True


    
        