from GamePieces import isLegalMove

class AI:

    def __init__(self, color):

        self.color = color

    def analyze(self, gameboard):

        movement = ()

        for i in range(8):
            for j in range(8):
                for m in range(8):
                    for n in range(8):

                        movement = (i, j, m, n)

                        if isLegalMove(gameboard, movement, self.color):
                            return movement

        print(movement)
        return None

