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


if __name__ == "__main__":
    for i in range(0,10):
        print(generatePuzzle(random.choice(difficulties)))
    

