# David Liben-Nowell
# CS 111, Carleton College
# sample.py
#
# A sample chunk of code to support some interactive buttons for projects.

from graphics import *


class chess:
    def __init__(self,lable,image, image2, hostality):
        self.hostality=hostality
        self.lable=lable
        self.image=image
        self.image2=image2
        self.hostality = hostality

class Footman(chess):
    def __init__(self):
        chess.__init__(self, "Footman",'footman1.gif',0)

class Duke(chess):
    def __init__(self):
        chess.__init__(self, "Duke", 'duke1.gif',0)

class Seer(chess):
    def __init__(self):
        chess.__init__(self, "Seer", 'seer1.gif',0)

class Pikeman(chess):
    def __init__(self):
        chess.__init__(self, "Pikeman", 'pikeman1.gif',0)

class Ranger(chess):
    def __init__(self):
        chess.__init__(self, "Ranger", image,0)

class Knight(chess):
    def __init__(self):
        chess.__init__(self, "Knight", 'knight1.gif',0)


class Champion(chess):
    def __init__(self):
        chess.__init__(self, "Champion", image,0)

class General(chess):
    def __init__(self):
        chess.__init__(self, "General", image,0)

class Bowman(chess):
    def __init__(self):
        chess.__init__(self, "Bowman", image,0)

class Wizard(chess):
    def __init__(self):
        chess.__init__(self, "Wizard", image,0)

class Dragoon(chess):
    def __init__(self):
        chess.__init__(self, "Dragoon", image,0)

class Longbowman(chess):
    def __init__(self):
        chess.__init__(self, "Longbowman", image,0)

class Assassin(chess):
    def __init__(self):
        chess.__init__(self, "Assassin", image,0)


class OppoFootman(chess):
    def __init__(self):
        chess.__init__(self, "Footman",'footman1.gif',1)

class OppoDuke(chess):
    def __init__(self):
        chess.__init__(self, "Duke", 'duke1.gif',1)

class OppoSeer(chess):
    def __init__(self):
        chess.__init__(self, "Seer", 'seer1.gif',1)

class OppoPikeman(chess):
    def __init__(self):
        chess.__init__(self, "Pikeman", 'pikeman1.gif',1)

class OppoRanger(chess):
    def __init__(self):
        chess.__init__(self, "Ranger", image,1)

class OppoKnight(chess):
    def __init__(self):
        chess.__init__(self, "Knight", image,1)


class OppoChampion(chess):
    def __init__(self):
        chess.__init__(self, "Champion", image,1)

class OppoGeneral(chess):
    def __init__(self):
        chess.__init__(self, "General", image,1)

class OppoBowman(chess):
    def __init__(self):
        chess.__init__(self, "Bowman", image,1)

class OppoWizard(chess):
    def __init__(self):
        chess.__init__(self, "Wizard", image,1)

class OppoDragoon(chess):
    def __init__(self):
        chess.__init__(self, "Dragoon", image,1)

class OppoLongbowman(chess):
    def __init__(self):
        chess.__init__(self, "Longbowman", image,1)

class OppoAssassin(chess):
    def __init__(self):
        chess.__init__(self, "Assassin", image,1)


class Button:
    def __init__(self, x, y, width, height, chess = False):
        self.xRange = [x, x + width]
        self.yRange = [y, y + height]
        self.rectangle = Rectangle(Point(x, y), Point(x + width, y + height))
        self.clicks = 0
        self.color = None
        self.rectangle.setFill("white")
        self.chess=chess
        self.moves = 0
        if chess:
            self.chesslable2 = chess.lable
            self.chesslable3 = chess.hostality
            self.chesslable = Text(Point(x+ (width/2), y+ (height/2)), chess.lable)
            self.chessImage = Image(Point(x+ (width/2), y+ (height/2)), chess.image)
            self.chesslable.setSize(22)
            if chess.hostality == 1:
                self.chesslable.setTextColor('red')
        else:
            self.chesslable2 = None




        
    def draw(self, window):
        self.rectangle.draw(window)
        if self.chess:
            self.chessImage.draw(window)

    def pointInside(self, point):
        return self.xRange[0] <= point.getX() <= self.xRange[1] \
            and self.yRange[0] <= point.getY() <= self.yRange[1] \

    def onClick(self):
        self.clicks += 1
        if self.clicks % 2 == 1:
            self.rectangle.setFill("blue")
        else:
            self.rectangle.setFill("white")

    def onRightClick(self):
        self.rectangle.setFill("red")

class ButtonWindow:
    def __init__(self, title, width, height, squares):
        self.window = GraphWin(title, width, height)
        self.window.setMouseHandler(self.handleClick)
        self.window.setMouseRightHandler(self.handleRightClick)
        self.lastupdate = time.time()
        self.squares = squares
        self.width = width
        self.height = height
        self.clicks = 1
        self.currentchess = None
        self.chesslastlocation = None
        self.chessnewlocation = None


    def update(self):
        self.window.update()

    def closed(self):
        return not self.window.winfo_exists()        

    def handleClick(self, point):
        cols = point.getX() / 120 
        rows = point.getY() / 120
        selectedsquare = self.squares[cols][rows]
        for i in range(6):
            for v in range(6):
                self.squares[i][v].rectangle.setFill('white')
        if self.clicks == 1 and selectedsquare and (selectedsquare.moves % 2 == 1):
            self.currentchess == selectedsquare.chess
            self.lastchesslocation = [rows,cols]
            if selectedsquare.chess.hostality == 0:
                self.FlipmoveDisplay(selectedsquare.chess, rows, cols)
            if selectedsquare.chess.hostality == 1:
                self.OppoFlipmoveDisplay(selectedsquare.chess, rows, cols)
            self.clicks = 2

        elif self.clicks == 1 and selectedsquare and (selectedsquare.moves % 2 == 0):
            self.currentchess == selectedsquare.chess
            self.lastchesslocation = [rows,cols]
            self.lastchess=self.squares[rows][cols]
            if selectedsquare.chess.hostality == 0:
                self.moveDisplay(selectedsquare.chess, rows, cols)
            if selectedsquare.chess.hostality == 1:
                self.OppomoveDisplay(selectedsquare.chess, rows, cols)
            self.clicks = 2

        elif self.clicks == 2:
            for squarerow in self.squares:
                for square in squarerow:
                    square.rectangle.setFill("white")
            self.newchess=selectedsquare
            self.nRow = rows
            self.nCol = cols
            self.chessnewlocation = [self.nRow,self.nCol]
            self.moveUnit(self.newchess)                      
            self.clicks = 1

        else:
            self.clicks = 1

    def handleRightClick(self, point):
        for square in self.squares:
            if square.pointInside(point):
                square.onRightClick()

    def draw(self):
        for squarerow in self.squares:
            for square in squarerow:
                square.draw(self.window)

    def moveUnit(self, newchess):
        w = (120*self.nCol)+120/2
        h = (120*self.nRow)+120/2
        # a = Text(Point(400,700),'Not A Valid Move!')
        # a.setSize(36)
        if self.squares[self.lastchesslocation[1]][self.lastchesslocation[0]].chess:
            if newchess.chess:
                newchess.chesslable.undraw()

            if newchess.chesslable2== "Duke":
                if newchess.chesslable3 == 0:
                    win = Text(Point(400,700),'You Lost!')
                    win.setSize(36)
                    win.draw(self.window)
                if newchess.chesslable3 == 1:
                    loss = Text(Point(400,700),'You Win!')
                    loss.setSize(36)
                    loss.draw(self.window)                    
            if newchess.color == "green" or newchess.color == "blue":
                newchess.chess, self.squares[self.lastchesslocation[1]][self.lastchesslocation[0]].chess = self.squares[self.lastchesslocation[1]][self.lastchesslocation[0]].chess, newchess.chess
                newchess.chesslable = Image(Point(w, h), newchess.chess.image)
                newchess.chesslable.draw(self.window)
                if newchess.chess.hostality == 1:
                    newchess.chesslable.setTextColor('red')                
                newchess.moves =  self.squares[self.lastchesslocation[1]][self.lastchesslocation[0]].moves + 1                
                self.squares[self.lastchesslocation[1]][self.lastchesslocation[0]].chessImage.undraw()

            # else:

            #     # a.draw(self.window)      
            # # if newchess.color == "red":
            # #     self.squares[self.nRow][self.nCol].chesslable.undraw()
            # #     newchess=lastchess

    def moveDisplay(self, selectedchess,col, row):
        if selectedchess.lable == "Footman":
            if row+1 <= 5:
                self.squares[row+1][col].rectangle.setFill('green')
                self.squares[row+1][col].color = 'green'
            if col+1 <= 5:
                self.squares[row][col+1].rectangle.setFill('green')
                self.squares[row][col+1].color = 'green'
            if row -1 >=0:
                self.squares[row-1][col].rectangle.setFill('green')
                self.squares[row-1][col].color = 'green'
            if col-1 >=0:
                self.squares[row][col-1].rectangle.setFill('green')
                self.squares[row][col-1].color = 'green'

        if selectedchess.lable == "Seer":
            if (row+1 <=5) and (col+1 <=5):
                self.squares[row+1][col+1].rectangle.setFill('green')
                self.squares[row+1][col+1].color = 'green'
            if (row+1 <=5) and (col-1 >=0):
                self.squares[row+1][col-1].rectangle.setFill('green')
                self.squares[row+1][col-1].color = 'green'
            if (row-1 >=0) and (col+1 <=5):
                self.squares[row-1][col+1].rectangle.setFill('green')
                self.squares[row-1][col+1].color = 'green'
            if (row-1>=0) and (col-1>=0):
                self.squares[row-1][col-1].rectangle.setFill('green')
                self.squares[row-1][col-1].color = 'green'
            if (row+2 <=5) and (col <=5):
                self.squares[row+2][col].rectangle.setFill('blue')
                self.squares[row+2][col].color = 'blue'                
            if (row-2 >=0) and (col <=5):
                self.squares[row-2][col].rectangle.setFill('blue')
                self.squares[row-2][col].color = 'blue'
            if (row <=5) and (col+2 <=5):
                self.squares[row][col+2].rectangle.setFill('blue')
                self.squares[row][col+2].color = 'blue'
            if (row <=5) and (col-2 >=0):
                self.squares[row][col-2].rectangle.setFill('blue')
                self.squares[row][col-2].color = 'blue'


        if selectedchess.lable == "Pikeman":            
            if (row+1 <=5) and (col-1 >=0):
                self.squares[row+1][col-1].rectangle.setFill('green')
                self.squares[row+1][col-1].color = 'green'
            if (row-1 >=0) and (col-1 >=0):
                self.squares[row-1][col-1].rectangle.setFill('green')
                self.squares[row-1][col-1].color = 'green'
            if (row+2 <=5) and (col-2 >=0):
                self.squares[row+2][col-2].rectangle.setFill('green')
                self.squares[row+2][col-2].color = 'green'
            if (row-2 >=0) and (col-2 >=0):
                self.squares[row-2][col-2].rectangle.setFill('green')
                self.squares[row-2][col-2].color = 'green'


        if selectedchess.lable == "Duke":
            for i in range(6):
                if i != row:
                    self.squares[i][col].rectangle.setFill('green')
                    self.squares[i][col].color = 'green'  

        if selectedchess.lable == "Knight":
            if (row+1 <= 5) and (col<=5):
                self.squares[row-1][col].rectangle.setFill('green')
                self.squares[row-1][col].color = 'green'
            if (row+1 <= 5) and (col<=5):
                self.squares[row-1][col-2].rectangle.setFill('green')
                self.squares[row-1][col-2].color = 'green'
            if (row+1 <= 5) and (col<=5):
                self.squares[row+1][col-2].rectangle.setFill('green')
                self.squares[row+1][col-2].color = 'green'
            if (row+1 <= 5) and (col<=5):
                self.squares[row+1][col].rectangle.setFill('green')
                self.squares[row+1][col].color = 'green'
            if (row+1 <= 5) and (col<=5):
                self.squares[row][col+2].rectangle.setFill('green')
                self.squares[row][col+2].color = 'green'
            if (row+1 <= 5) and (col<=5):
                self.squares[row][col+1].rectangle.setFill('green')
                self.squares[row][col+1].color = 'green'
            # if (row <= 5) and (col-1 >=0):
            #     self.squares[col-1][row].rectangle.setFill('green')
            #     self.squares[col-1][row].color = 'green'
            # if (row <=5) and (col-2 >=0):
            #     self.squares[col][row-2].rectangle.setFill('green')
            #     self.squares[col][row-2].color = 'green'
            # if (col-1 >=0) and (row <= 5):
            #     self.squares[col][row-1].rectangle.setFill('green')
            #     self.squares[col][row-1].color = 'green'
            # if (col+2 <=5) and (row-1 >=0):
            #     self.squares[col-1][row+2].rectangle.setFill('green')
            #     self.squares[col-1][row+2].color = 'green'
            # if (col-2 >=0) and (row-1 >=0):
            #     self.squares[col-1][row-2].rectangle.setFill('green')
            #     self.squares[col-1][row-2].color = 'green'

    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":            
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":

    def FlipmoveDisplay(self,selectedchess,col,row):
        if selectedchess.lable == "Footman":
            if (row+1 <=5) and (col+1 <=5):
                self.squares[row+1][col+1].rectangle.setFill('green')
                self.squares[row+1][col+1].color = 'green'
            if (row+1 <=5) and (col -1 >=0):
                self.squares[row+1][col-1].rectangle.setFill('green')
                self.squares[row+1][col-1].color = 'green'
            if (row-1 >=0) and (col+1 <=5):
                self.squares[row-1][col+1].rectangle.setFill('green')
                self.squares[row-1][col+1].color = 'green'
            if (row-1 >=0) and (col-1 >=0):
                self.squares[row-1][col-1].rectangle.setFill('green')
                self.squares[row-1][col-1].color = 'green'
            if (row <=5) and (col-2 >=0):
                self.squares[row][col-2].rectangle.setFill('green')
                self.squares[row][col-2].color = 'green'

        if selectedchess.lable == "Seer":
            if (row+1 <=5) and (col <=5):
                self.squares[row+1][col].rectangle.setFill('green')
                self.squares[row+1][col].color = 'green'
            if (row <=5) and (col+1 <=5):
                self.squares[row][col+1].rectangle.setFill('green')
                self.squares[row][col+1].color = 'green'
            if (row-1>=0) and (col <=5):
                self.squares[row-1][col].rectangle.setFill('green')
                self.squares[row-1][col].color = 'green'
            if (row <=5) and (col-1 >=0):
                self.squares[row][col-1].rectangle.setFill('green')
                self.squares[row][col-1].color = 'green'
            if (row+2 <=5) and (col+2 <=5):
                self.squares[row+2][col+2].rectangle.setFill('blue')
                self.squares[row+2][col+2].color = 'blue'
            if (row-2 >=0) and (col-2 >=0):
                self.squares[row-2][col-2].rectangle.setFill('blue')
                self.squares[row-2][col-2].color = 'blue'
            if (row-2 >=0) and (col+2 <=5):
                self.squares[row-2][col+2].rectangle.setFill('blue')
                self.squares[row-2][col+2].color = 'blue'
            if (row+2 <=5) and (col-2 >=0):
                self.squares[row+2][col-2].rectangle.setFill('blue')
                self.squares[row+2][col-2].color = 'blue'

        if selectedchess.lable == "Pikeman":
            if (row <=5) and (col+1 <=5):
                self.squares[row][col+1].rectangle.setFill('green')
                self.squares[row][col+1].color = 'green'
            if (row <=5) and (col-1>=0):
                self.squares[row][col-1].rectangle.setFill('green')
                self.squares[row][col-1].color = 'green'
            if (row <=5) and (col+2 <=5):
                self.squares[row][col+2].rectangle.setFill('green')
                self.squares[row][col+2].color = 'green'
            if (row-1 >=0) and (col-2 >=0):
                self.squares[row-1][col-2].rectangle.setFill('green')
                self.squares[row-1][col-2].color = 'green'
            if (row+1 <=5) and (col-2>=0):
                self.squares[row+1][col-2].rectangle.setFill('green')
                self.squares[row+1][col-2].color = 'green'


        if selectedchess.lable == "Duke":
            for i in range(6):
                if i != col:
                    self.squares[row][i].rectangle.setFill('green')
                    self.squares[row][i].color = 'green'  



    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":            
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":        
    def OppomoveDisplay(self, selectedchess,col, row):
        if selectedchess.lable == "Footman":
            if row+1 <= 5:
                self.squares[row+1][col].rectangle.setFill('green')
                self.squares[row+1][col].color = 'green'
            if col+1 <= 5:
                self.squares[row][col+1].rectangle.setFill('green')
                self.squares[row][col+1].color = 'green'
            if row -1 >=0:
                self.squares[row-1][col].rectangle.setFill('green')
                self.squares[row-1][col].color = 'green'
            if col-1 >=0:
                self.squares[row][col-1].rectangle.setFill('green')
                self.squares[row][col-1].color = 'green'

        if selectedchess.lable == "Seer":
            if (row+1 <=5) and (col+1 <=5):
                self.squares[row+1][col+1].rectangle.setFill('green')
                self.squares[row+1][col+1].color = 'green'
            if (row+1 <=5) and (col-1 >=0):
                self.squares[row+1][col-1].rectangle.setFill('green')
                self.squares[row+1][col-1].color = 'green'
            if (row-1 >=0) and (col+1 <=5):
                self.squares[row-1][col+1].rectangle.setFill('green')
                self.squares[row-1][col+1].color = 'green'
            if (row-1>=0) and (col-1>=0):
                self.squares[row-1][col-1].rectangle.setFill('green')
                self.squares[row-1][col-1].color = 'green'
            if (row+2 <=5) and (col <=5):
                self.squares[row+2][col].rectangle.setFill('blue')
                self.squares[row+2][col].color = 'blue'                
            if (row-2 >=0) and (col <=5):
                self.squares[row-2][col].rectangle.setFill('blue')
                self.squares[row-2][col].color = 'blue'
            if (row <=5) and (col+2 <=5):
                self.squares[row][col+2].rectangle.setFill('blue')
                self.squares[row][col+2].color = 'blue'
            if (row <=5) and (col-2 >=0):
                self.squares[row][col-2].rectangle.setFill('blue')
                self.squares[row][col-2].color = 'blue'


        if selectedchess.lable == "Pikeman":            
            if (row+1 <=5) and (col+1 <=5):
                self.squares[row+1][col+1].rectangle.setFill('green')
                self.squares[row+1][col+1].color = 'green'
            if (row-1 >=0) and (col-1 >=0):
                self.squares[row-1][col-1].rectangle.setFill('green')
                self.squares[row-1][col-1].color = 'green'
            if (row+2 <=5) and (col+2 <=5):
                self.squares[row+2][col+2].rectangle.setFill('green')
                self.squares[row+2][col+2].color = 'green'
            if (row-2 >=0) and (col-2 >=0):
                self.squares[row-2][col-2].rectangle.setFill('green')
                self.squares[row-2][col-2].color = 'green'


        if selectedchess.lable == "Duke":
            for i in range(6):
                if i != row:
                    self.squares[i][col].rectangle.setFill('green')
                    self.squares[i][col].color = 'green'  


    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":            
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":

    def OppoFlipmoveDisplay(self,selectedchess,col,row):
        if selectedchess.lable == "Footman":
            if (row+1 <=5) and (col+1 <=5):
                self.squares[row+1][col+1].rectangle.setFill('green')
                self.squares[row+1][col+1].color = 'green'
            if (row+1 <=5) and (col -1 >=0):
                self.squares[row+1][col-1].rectangle.setFill('green')
                self.squares[row+1][col-1].color = 'green'
            if (row-1 >=0) and (col+1 <=5):
                self.squares[row-1][col+1].rectangle.setFill('green')
                self.squares[row-1][col+1].color = 'green'
            if (row-1 >=0) and (col-1 >=0):
                self.squares[row-1][col-1].rectangle.setFill('green')
                self.squares[row-1][col-1].color = 'green'
            if (row <=5) and (col+2 <=5):
                self.squares[row][col+2].rectangle.setFill('green')
                self.squares[row][col+2].color = 'green'

        if selectedchess.lable == "Seer":
            if (row+1 <=5) and (col <=5):
                self.squares[row+1][col].rectangle.setFill('green')
                self.squares[row+1][col].color = 'green'
            if (row <=5) and (col+1 <=5):
                self.squares[row][col+1].rectangle.setFill('green')
                self.squares[row][col+1].color = 'green'
            if (row-1>=0) and (col <=5):
                self.squares[row-1][col].rectangle.setFill('green')
                self.squares[row-1][col].color = 'green'
            if (row <=5) and (col-1 >=0):
                self.squares[row][col-1].rectangle.setFill('green')
                self.squares[row][col-1].color = 'green'
            if (row+2 <=5) and (col+2 <=5):
                self.squares[row+2][col+2].rectangle.setFill('blue')
                self.squares[row+2][col+2].color = 'blue'
            if (row-2 >=0) and (col-2 >=0):
                self.squares[row-2][col-2].rectangle.setFill('blue')
                self.squares[row-2][col-2].color = 'blue'
            if (row-2 >=0) and (col+2 <=5):
                self.squares[row-2][col+2].rectangle.setFill('blue')
                self.squares[row-2][col+2].color = 'blue'
            if (row+2 <=5) and (col-2 >=0):
                self.squares[row+2][col-2].rectangle.setFill('blue')
                self.squares[row+2][col-2].color = 'blue'

        if selectedchess.lable == "Pikeman":
            if (row <=5) and (col+1 <=5):
                self.squares[row][col+1].rectangle.setFill('green')
                self.squares[row][col+1].color = 'green'
            if (row <=5) and (col-1>=0):
                self.squares[row][col-1].rectangle.setFill('green')
                self.squares[row][col-1].color = 'green'
            if (row <=5) and (col-2 >=0):
                self.squares[row][col-2].rectangle.setFill('green')
                self.squares[row][col-2].color = 'green'
            if (row+1 <=5) and (col+2 <=5):
                self.squares[row+1][col+2].rectangle.setFill('red')
                self.squares[row+1][col+2].color = 'red'
            if (row-1 >=0) and (col+2 <=5):
                self.squares[row-1][col+2].rectangle.setFill('red')
                self.squares[row-1][col+2].color = 'red'

        if selectedchess.lable == "Duke":
            for i in range(6):
                if i != col:
                    self.squares[row][i].rectangle.setFill('green')
                    self.squares[row][i].color = 'green'  



    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":            
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":
    #     if selectedchess.lable == "Pikeman":        

def main():
    squares = []
    for row in range(6):
        squares.append([])
        for col in range(6):     
            if row == 3 and col == 5:
                squares[row].append(Button(row * 120, col * 120, 120, 120, Footman()))
            elif row == 2 and col == 5:
                squares[row].append(Button(row * 120, col * 120, 120, 120, Duke()))
            elif row == 2 and col == 4:
                squares[row].append(Button(row * 120, col * 120, 120, 120, Footman()))
            elif row == 3 and col == 0:
                squares[row].append(Button(row * 120, col * 120, 120, 120, OppoFootman()))
            elif row == 2 and col == 0:
                squares[row].append(Button(row * 120, col * 120, 120, 120, OppoDuke()))
            elif row == 2 and col == 1:
                squares[row].append(Button(row * 120, col * 120, 120, 120, OppoFootman()))           
            elif row == 2 and col == 3:
                squares[row].append(Button(row * 120, col * 120, 120, 120, Knight()))                    
            else:
                squares[row].append(Button(row * 120, col * 120, 120, 120))
    window = ButtonWindow("Game board",1200, 1200, squares)
    # a = Image(Point(100,200), 'footman1.gif')
    # a.draw(window)
    window.draw()
    while not window.closed():
        window.update() 

if __name__ == "__main__":
    main()
