# David Liben-Nowell
# CS 111, Carleton College
# project.py
#
# A sample chunk of code to support the handling of mouse clicks and
# key presses in real time.

from graphics import *
import random
import time

class ClickableWindow:
    def __init__(self, title, width, height):
        self.window = GraphWin(title, width, height)
        self.window.setMouseHandler(self.handleClick)
        self.window.master.bind("<Key>",self.handleKeyPress)
        self.lastkey = None
        self.circle = Circle(Point(width / 5, height / 3),10)
        self.circle.setFill(color_rgb(0,0,0))
        self.circle.draw(self.window)
        self.lastupdate = time.time()

    # Do some processing "every once in a while" -- if it's been a
    # least a quarter of a second since the color of the circle in
    # this window was redrawn with a new color, then redraw it.
    def update(self):
        if time.time() - self.lastupdate > 0.25:
            self.circle.setFill(color_rgb(random.randint(0,255),
                                          random.randint(0,255),
                                          random.randint(0,255)))
            self.lastupdate = time.time()
        self.window.update()

    # Returns True if and only if this window has been closed.
    def closed(self):
        return not self.window.winfo_exists()        

    def handleClick(self,point):
        # This code will be executed whenever the left mouse button is
        # clicked, and the value passed in as point will be the
        # location on the screen where the click occurred.  For kicks,
        # I've chosen to display a red circle at the point of the
        # click.  You can get the x and y coordinates via point.getX()
        # and point.getY().
        c = Circle(point,3)
        c.setFill(color_rgb(255,0,0))
        c.draw(self.window)

    def handleKeyPress(self,key):
        # This code will be executed whenever a key is pressed, and
        # the value passed in as key will represent the key that was
        # pressed.  You can get the character representing the pressed
        # key using key.char.  For kicks, I've chosen to display the
        # last pressed key in a text box at the upper left of the
        # window, by undrawing the previous text and then writing the
        # new text.  If the character is 'q', then the program quits.
        if key.char == "q":
            Text(Point(100,50),"close the window to quit").draw(self.window)
        else:
            if self.lastkey:
                self.lastkey.undraw()
            t = Text(Point(20,20),key.char)
            t.draw(self.window)
            self.lastkey = t

def main():
    print "Close the window to quit."
    win = ClickableWindow("Game Sample", 500, 300)
    
    while not win.closed():
        win.update()

if __name__ == "__main__":
    main()
