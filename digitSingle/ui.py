from grid import SudokuGrid
from box import SudokuBox

def getPossibility(num,cell:SudokuBox):
    if cell.known:
        if num == 5:
            return str(cell.value)
        else:
            return " "
    if num in cell.options:
        return str(num)
    return " "

def showEntireGrid(grid:SudokuGrid,message=""):
    for rowNum in range(9):
        string1 = ""
        string2 = ""
        string3 = ""
        string4 = ""
        for colNum in range(9):
            cell = grid.getCell(rowNum,colNum)
            string1 += " "
            string2 += " "
            string3 += " "
            string4 += " "
            
            string1 += getPossibility(1,cell)
            string1 += getPossibility(2,cell)
            string1 += getPossibility(3,cell)
            string2 += getPossibility(4,cell)
            string2 += getPossibility(5,cell)
            string2 += getPossibility(6,cell)
            string3 += getPossibility(7,cell)
            string3 += getPossibility(8,cell)
            string3 += getPossibility(9,cell)
            string1 += " "
            string2 += " "
            string3 += " "
            string4 += "____"
            if colNum != 8:
                string1 += "|"
                string2 += "|"
                string3 += "|"
                string4 += "|"
            if colNum in (2,5):
                string1 += "||"
                string2 += "||"
                string3 += "||"
                string4 += "||"
        print(string1)
        print(string2)
        print(string3)
        if rowNum not in [2,5,8]:
            print(string4)
        if rowNum in (2,5):
            print("=================|||=================|||=================")
    print(message)

