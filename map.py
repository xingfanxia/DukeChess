from graphics import *
from images import *
from buttons import *

class Grassland:
	def __init__(self, window): 
		self.rows = 20
		self.cols = 20
		self.length = 50
		self.xPos = 100
		self.yPos = 100
		self.window = window

	def Rect(self):
		for i in range(self.rows):
			for v in range(self.cols):
				Rectangle(Point(self.xPos,self.yPos),Point(self.xPos+i*self.length,self.yPos+v*self.length)).draw(self.window)

# class player(Grassland):
# 	def __init__(self, image, xPos, yPos            )


def main():
	squares=[]
	window = ButtonWindow("grass", 1200, 1200, squares)
	a = Grassland(window)
	a.Rect()
	res = raw_input("enter x to exit")
main()