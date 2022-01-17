import subprocess, random

difficulties = ['simple','easy','intermediate','expert']



def generatePuzzle(difficulty):
    command = "qqwing --generate --difficulty "+difficulty+" --compact"
    puzzle = subprocess.check_output(command.split())
    puzzleList = convertPuzzle(puzzle)
    return convertPuzzle(puzzleList)

def convertPuzzle(puzzleIn):
    return(chunks(puzzleIn,9))

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def rowReduction(lst):
    puzzle.append(lst[0:8])
    puzzle.append(lst[9:17])
    puzzle.append(lst[18:26])
    puzzle.append(lst[27:35])
    puzzle.append(lst[36:44])
    puzzle.append(lst[45:53])
    puzzle.append(lst[54:62])
    puzzle.append(lst[63:71])
    puzzle.append(lst[72:80])
    return puzzle



if __name__ == "__main__":
    for i in range(0,10):
        print(generatePuzzle(random.choice(difficulties)))
    

