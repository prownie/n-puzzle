from tkinter import *
from math import sqrt
import time

class ResultPrinter(Tk):
	index = 0

	def __init__(self, pathList):
		self.pathList = pathList
		self.size = size = int(sqrt(len(pathList[0])))
		self.actualPuzzle = pathList[0]
		self.printResult()

	def drawCanvas(self):
		print("drawing")
		self.canvas = Canvas(self.window,width=self.size*150,height=150*self.size)
		self.canvas.pack()
		self.items=[None for i in range(17)]
		for row in range (0,self.size):
			for column in range (0,self.size):
				rect = self.canvas.create_rectangle(column*150,row*150,(column+1)*150,(row+1)*150)
				txt = self.canvas.create_text(column*150+75,row*150+75,text=str(self.actualPuzzle[row*self.size+column]),font=('Helvetica','30','bold'), tags="number")
				self.items[self.actualPuzzle[row*self.size+column]] = (rect, txt)

	def drawNumbers(self):
		print("drawNumbers")
		for row in range (0,self.size):
			for column in range (0,self.size):
				txt = self.canvas.create_text(column*150+75,row*150+75,text=str(self.actualPuzzle[row*self.size+column]),font=('Helvetica','30','bold'), tags="number")

	def leftKey(self, event):
		if self.index > 0:
			self.canvas.delete("number")
			self.index = self.index -1
			self.actualPuzzle = self.pathList[self.index]
			self.drawNumbers()
			# self.moveTile("left")
	
	def rightKey(self, event):
		if self.index < len(self.pathList)-1:
			self.canvas.delete("number")
			self.index = self.index +1
			self.actualPuzzle = self.pathList[self.index]
			self.drawNumbers()
			# self.moveTile("right")

	def moveTile(self, way):
		print("in move")
		if way == "left" and self.index >= 0:
			previous = self.pathList[self.index+1]
			print(previous)
			for i in range (0,self.size*self.size):
				if (self.actualPuzzle[i] != 0 and self.actualPuzzle[i] != previous[i]):
					print("previous index"+str(previous.index(self.actualPuzzle[i]))+" actual index="+str(i))
					# print("diff found for number"+str(self.actualPuzzle[i])+"at index "+str(i),": ",previous.index(self.actualPuzzle[i]))
					print(self.canvas.gettags("5"))
					rect, txt = self.items[previous[i]]
					self.canvas.move(rect, (previous.index(self.actualPuzzle[i])/self.size - i/self.size) * 150, (previous.index(self.actualPuzzle[i])%self.size - i%self.size)/150)
		if way == "right" and self.index < len(self.pathList):
			previous = self.pathList[self.index-1]
			print(previous)
	

	def printResult(self):
		self.window = Tk()
		self.window.title("Puzzle result")
		resolution = str(self.size*150)+'x'+str(self.size*150)
		self.window.geometry(resolution)
		self.drawCanvas()
		self.window.bind('<Left>', self.leftKey)
		self.window.bind('<Right>', self.rightKey)
		self.window.mainloop()