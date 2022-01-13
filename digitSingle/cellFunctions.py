from cell import SudokuCell

def populateCells(list):
    cells = []
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
            cells.append(cell)
    return cells