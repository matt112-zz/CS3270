# I Matthew Castro wrote this

import sys
import re

class Puzzle:
    def __init__(self, lines):
        self.puzzle = ''.join(lines) #create a single string of the entire puzzle
        self.width = len(lines[0])
        self.spacer = '.' * (self.width - 1) #for regex the period is used as a metacharacter. Replacement for any character
    def getWidth(self):
        return self.width
    def search(self, word):
        yield re.search(word, self.puzzle) # right
        yield re.search(''.join(reversed(word)), self.puzzle) # left
        yield re.search(self.spacer.join(word), self.puzzle) # down 
        yield re.search(self.spacer.join(''.join(reversed(word))), self.puzzle) # up
        yield re.search((self.spacer + '.').join(word), self.puzzle) # down right
        yield re.search((self.spacer + '.').join(''.join(reversed(word))), self.puzzle) # up left
        yield re.search(self.spacer[1:].join(word), self.puzzle) # down left
        yield re.search(self.spacer[1:].join(''.join(reversed(word))), self.puzzle) # up right
           
        
myLines = open((sys.argv[1]), 'r').readlines()

fileInput = [n.strip() for n in myLines]

lines = fileInput[:fileInput.index("")]
words = fileInput[fileInput.index("")+1:]

p1 = Puzzle(lines)
width = p1.getWidth()

dirs = ('right', 'left', 'down', 'up', 
        'down right', 'up left', 'down left', 'up right')
 
for word in words:
    for index, match in enumerate(p1.search(word)):
        if match is not None:
            #position depends on which direction the match was
            pos = match.end() - 1 if index % 2 else match.start()

            row = pos / width
            column = pos % width
   
            # Calculate the coordinates for the word based on the direction it was going
            if dirs[index] == 'right':
                startCoor = (row, column)
                endCoor = (row , column+len(word)-1)
            elif dirs[index] == 'left':
                startCoor = (row, column)
                endCoor = (row, column-len(word)+1)
            elif dirs[index] == 'down':
                startCoor = (row, column)
                endCoor = (row + len(word)-1, column)
            elif dirs[index] == 'up':
                startCoor = (row, column)
                endCoor = (row- len(word)+1, column)
            elif dirs[index] == 'down right':
                startCoor = (row, column)
                endCoor = (row + len(word)-1, column + len(word) -1)
            elif dirs[index] == 'up left':
                startCoor = (row, column)
                endCoor = (row - len(word)+1, column-len(word)+1)
            elif dirs[index] == 'down left':
                startCoor = (row, column)
                endCoor = (row - len(word)+1, column - len(word)+1)
            elif dirs[index] == 'up right':   
                startCoor = (row, column)
                endCoor = (row + len(word)-1, column + len(word)-1)
                  
            print word, 'found at start: ' + str(startCoor[0]) + ', ' + str(startCoor[1]) + ' end ' + str(endCoor[0]) + ', ' + str(endCoor[1])
            break #stops the for loop from continuing the search function. Once a match is found we are done.
    else:
        print word, 'not found'