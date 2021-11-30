
class DistanceInfo():
    xPosition = None
    yPosition = None
    distance = None
    Knight = None
    isSolution = False
    isEnd = False
    solutionParents = [] # of type Knight
    solutionsWithDistance = []
    parent = None

    def __init__(self, x, y):
        self.xPosition = x
        self.yPosition = y
        self.distance = None
        self.Knight = None
        self.isSolution = False
        self.isEnd = False
        self.solutionParents = [] # of type Knight
        self.solutionsWithDistance = []
        self.parent = None
