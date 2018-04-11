
from PIL import Image

class View:

    image = "images/BlackKing.png"

    def generateImage(self, gameboard):

        imgSize = 120

        new_im = Image.new('RGB', (8*imgSize, 8*imgSize))

        for i in range(len(gameboard)):
            for j in range(len(gameboard[i])):

                square = gameboard[i][j]

                #if

                if i%2 != j%2:
                    imgPath = "images/LightTile.png"

                elif square == None:
                    imgPath = "images/DarkTile.png"


                else:

                    if square.color == "R":
                        color = "Red"

                    else:
                        color = "Black"

                    if square.king:
                        description = "King"

                    else:
                        description = "Piece"

                    imgPath = "images/" + color + description + ".png"


                im = Image.open(imgPath)
                new_im.paste(im, (i*imgSize, j*imgSize))

        new_im.save('images/final.jpg')

        f = open('images/final.jpg', 'rb')
        return f.read()
