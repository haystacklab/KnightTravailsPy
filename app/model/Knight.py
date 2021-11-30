class Knight():
    possibleMoves = []
    moveSet = [
        [-1, -2],
        [-2, -1],
        [-2, +1],
        [-1, +2],
        [+1, -2],
        [+2, -1],
        [+2, +1],
        [+1, +2],
    ]
    def __init__(self, xPosition, yPosition):
        self.possibleMoves = []  # 1
        self.xPosition = xPosition # 1
        self.yPosition = yPosition # 1
        self.findPossibleMoves()  # 8

    def findPossibleMoves(self):
        for move in self.moveSet:  # 8
            newXPos = self.xPosition + move[0]
            newYPos = self.yPosition + move[1]
            if 0 <= newXPos <= 7 and 0 <= newYPos <= 7:
                self.possibleMoves.append([newXPos, newYPos])
        print("Possible moves for " + str(self.xPosition) + " , " + str(self.yPosition) + " : "
              + str(self.possibleMoves))
