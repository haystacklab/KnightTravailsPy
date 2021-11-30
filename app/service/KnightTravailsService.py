from app.service.KnightTravails import KnightTravails

def runKnightTravails(start, finish):
    newKnightTravails = KnightTravails()
    return newKnightTravails.findKnightMoves(start, finish)

