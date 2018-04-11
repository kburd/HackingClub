
def isLegalMove(board, movement, playerColor):

    startX, startY, endX, endY = movement

    #Piece off of board
    if endY > 7 or endY < 0 or endX > 7 or endX < 0:
        return False

    #No piece at start position
    elif board[startX][startY] == None:
        return False

    #Wrong color piece
    elif board[startX][startY].color != playerColor:
        return False

    #Movement not diagonal
    elif endX == startX or endY == startY:
        return False

    #Can not move to a light square
    elif endX%2 != endY%2:
        return False

    #Can not move on a space with a piece
    elif board[endX][endY] != None:
        return False

    #Can not move more than two spaces
    elif abs(endX-startX) > 2 or abs(endY-startY) > 2:
        return False

    #Pawns Must move one way
    elif board[startX][startY].king == False:

        #Red pawns must move high indexes to low indexes
        if playerColor == "R" and startX < endX:
            return False

        # Black pawns must move low indexes to high indexes
        if playerColor == "B" and startX > endX:
            return False


    #Check Jumps
    if abs(endX-startX) == 2 and abs(endY-startY) == 2:

        middlePiece = board[min(startX, endX)+1][min(startY, endY)+1]

        if middlePiece == None:
            return False

        if middlePiece.color == "R" and playerColor == "R":
            return False

        if middlePiece.color == "B" and playerColor == "B":
            return False

    return True

class Game:

    def __init__(self):

        self.gameBoard = []
        for i in range(8):
            row = []
            for j in range(8):
                if i < 3 and i % 2 == j % 2:
                    row += [Piece("B")]
                elif i > 4 and i % 2 == j % 2:
                    row += [Piece("R")]
                else:
                    row += [None]

            self.gameBoard += [row]

        self.numOfMoves = 0

    def __str__(self):
        string = ""
        for i in range(8):
            for j in range(8):
                square = self.gameBoard[i][j]
                if square == None:
                    square = "_"
                string += str(square)
            string += "\n"
        return string

    def movePiece(self, movement):

        startX, startY, endX, endY = movement

        piece = self.gameBoard[startX][startY]
        self.gameBoard[startX][startY] = None
        self.gameBoard[endX][endY] = piece

        #Check Jumps
        if abs(endX-startX) == 2 and abs(endY-startY) == 2:

            self.gameBoard[min(startX, endX)+1][min(startY, endY)+1] = None


        if endX == 0 and piece.color == "R":
            piece.king = True

        if endX == 7 and piece.color == "B":
            piece.king = True

class Piece:

    def __init__(self, color):

        self.color = color
        self.king = False

    def __str__(self):

        return self.color
