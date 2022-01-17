from dataclasses import replace
from solve import findSolutions
import subprocess, random, json

difficulties = ['simple','easy','intermediate','expert']

def addPuzzleToDict(name,puzzle,difficulty):
        fileName = "/data/puzzles.json"
        f = open(fileName)
        try:
                dataIn = json.load(f)
                dataIn[name] = {
                        'difficulty':difficulty,
                        'problem':puzzle
                }
        except:
                dataIn = {
                        name:
                                {
                                'difficulty':difficulty,
                                'problem':puzzle
                                }
                        }
        with open(fileName,"w+") as outfile:
                json.dump(dataIn,outfile)

def saveFile(seed,puzzle,solution,difficulty):
    dict = {
        'difficulty': diff,
        'problem': puzzle,
        'solution': solution
    }
    fileName = "/data/"+difficulty+"-"+str(seed)+".json"
    with open(fileName,'w') as fp:
        json.dump(dict,fp)


def generatePuzzle(difficulty):
    command = "qqwing --generate --difficulty "+difficulty+" --compact"
    puzzle = subprocess.check_output(command.split())
    puzzleList = convertPuzzle(puzzle)
    return puzzleList    
    #return convertPuzzle(puzzleList)

def convertPuzzle(puzzleStringIn):
    replacedString = []
    for char in puzzleStringIn:
        if chr(char) == "\n":
            continue
        if char == 46:
            replacedString.append(0)
        else:
            replacedString.append(int(chr(char)))
    
    # return replacedString
    return(rowReduction(replacedString))

def rowReduction(lst):
    puzzle = []
    puzzle.append(lst[0:9])
    puzzle.append(lst[9:18])
    puzzle.append(lst[18:27])
    puzzle.append(lst[27:36])
    puzzle.append(lst[36:45])
    puzzle.append(lst[45:54])
    puzzle.append(lst[54:63])
    puzzle.append(lst[63:72])
    puzzle.append(lst[72:81])
    return puzzle


if __name__ == "__main__":
    for i in range(0,10):
        seed = random.randint(1,1000000)
        diff = random.choice(difficulties)
        print("Generating {} puzzle, reference: {}".format(diff,seed))
        puzzle = generatePuzzle(diff)
        addPuzzleToDict(seed,puzzle,diff)

    findSolutions()
    

