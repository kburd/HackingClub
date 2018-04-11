from AI import *
from GamePieces import Game, isLegalMove


class Model:

    def __init__(self):

        self.game = Game()
        self.player = 0
        self.playerOne = AI("R")
        self.playerTwo = AI("B")

    def update(self):

        if self.player == 0:
            color = "R"
            movement = self.playerOne.analyze(self.game.gameBoard)

        else:
            color = "B"
            movement = self.playerTwo.analyze(self.game.gameBoard)

            if movement == None:
                return

        if isLegalMove(self.game.gameBoard, movement, color):
            self.game.movePiece(movement)

        else:
            print("Illegal Move")
            raise Exception

        self.player = (self.player+1)%2
