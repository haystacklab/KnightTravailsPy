from app.model import DistanceInfo
from app.model import Knight

class KnightTravails():

    distanceInfo = [[]] * 8
    def __init__(self):
        self.findDistanceInfo()

    def findDistanceInfo(self):
        self.distanceInfo = [[]] * 8
        for i in range(0, 8):
            self.distanceInfo[i] = [None] * 8
            for j in range(0, 8):
                self.distanceInfo[i][j] = DistanceInfo(i, j)

    def findKnightMoves(self, start, finish):
        print("start position: " + str(start))
        print("finish position: " + str(finish))
        startKnight = Knight(start[0], start[1])  # 1
        endKnight = Knight(finish[0], finish[1]) # 1

        self.distanceInfo[start[0]][start[1]].distance = 0 # 1
        self.distanceInfo[finish[0]][finish[1]].isEnd = True # 1
        self.distanceInfo[finish[0]][finish[1]].distance = 0 # 1

        solutionFound = False # 1

        positionsQueue = [] # 1

        positionsQueue.append(startKnight)  # 1

        while solutionFound is not True: # n
            currentKnight = positionsQueue.pop(0)  # n.1
            for move in currentKnight.possibleMoves: # n.n
                # print(move)
                currentDistanceInfo = self.distanceInfo[move[0]][move[1]] # 1
                if currentDistanceInfo.distance is None: # 1
                    currentDistanceInfo.Knight = Knight(move[0], move[1]) # 1
                    currentDistanceInfo.distance = self.distanceInfo[currentKnight.xPosition][currentKnight.yPosition].distance + 1  # 1
                    currentDistanceInfo.parent = currentKnight  # 1
                    positionsQueue.append(currentDistanceInfo.Knight)  # 1

                elif currentDistanceInfo.isEnd is True:  # 1
                    totalDistance = {
                        "position": [currentKnight.xPosition, currentKnight.yPosition],
                        "path": self.findPath(currentKnight, endKnight),
                        "distance": self.distanceInfo[currentKnight.xPosition][currentKnight.yPosition].distance + 1
                    }  # 1
                    currentDistanceInfo.solutionsWithDistance.append(totalDistance)  # 1
                    currentDistanceInfo.solutionParents.append(currentKnight)  # 1

                    self.distanceInfo[currentKnight.xPosition][currentKnight.yPosition].isSolution = True  # 1
            endKnightPossibleMoves = endKnight.possibleMoves  # n.1
            recordedEndKnightSolns = self.distanceInfo[endKnight.xPosition][endKnight.yPosition].solutionParents  # n.1
            if len(endKnightPossibleMoves) == len(recordedEndKnightSolns):  # n.1
                solutionFound = True  # n.1
        
        # print(self.distanceInfo)
        self.printSolns(endKnight)
        return self.distanceInfo[endKnight.xPosition][endKnight.yPosition].solutionsWithDistance  # 1

    
    def printSolns(self, endKnight):
        for soln in self.distanceInfo[endKnight.xPosition][endKnight.yPosition].solutionsWithDistance:
            print(soln)

    def findPath(self, currentKnight, endKnight):
        distance = 63
        path = [[endKnight.xPosition, endKnight.yPosition]]
        while distance > 0:
            if not currentKnight:
                print("error! current knight not found inspite of distance greater than 0, please check; dist: " + distance)
                break
            while self.distanceInfo[currentKnight.xPosition][currentKnight.yPosition].distance < distance:
                path.append([currentKnight.xPosition, currentKnight.yPosition])
                distance = self.distanceInfo[currentKnight.xPosition][currentKnight.yPosition].distance
                currentKnight = self.distanceInfo[currentKnight.xPosition][currentKnight.yPosition].parent
                if not currentKnight:
                    break
        path.reverse()
        # print("final traversed path: ")
        # print(" , ".join(map(str, path)))
        # print()
        return path

    def findPathSimple(self, currentKnight, endKnight):
        path = [[endKnight.xPosition, endKnight.yPosition]]
        while currentKnight is not None: # n max: 63
            path.append([currentKnight.xPosition, currentKnight.yPosition])
            distance = self.distanceInfo[currentKnight.xPosition][currentKnight.yPosition].distance
            currentKnight = self.distanceInfo[currentKnight.xPosition][currentKnight.yPosition].parent
        path.reverse()
        return path

