import tkinter as tk
import time

class Application(tk.Frame):
	w = 20
	h = 20
	size = 2
	snakeColor = 'yellow'
	backgroundColor = 'black'
	xpos = 10
	ypos = 10
	direction = 0
	def __init__(self,master = None):
		tk.Frame.__init__(self,master)

		self.grid(ipadx = 0, ipady = 0, padx = 0,pady = 0)
		self.squares = [[0 for x in range(self.w+1)] for x in range(self.w+1)]
		self.dataSquares = [[0 for x in range(self.w+1)] for x in range(self.w+1)]
		self.createWidgets()
		self.createWidgets()

		self.bind_all('<Key-Up>', self.keyPressHandler)
		self.bind_all('<Key-Left>', self.keyPressHandler)
		self.bind_all('<Key-Right>', self.keyPressHandler)
		self.bind_all('<Key-Down>', self.keyPressHandler)

		self.colorSquareSnake(self.xpos,self.ypos)

	def createWidgets(self):
		self.quit = tk.Button(self, text='Quit', command=self.quit)
		self.quit.grid(column = 0,row = 0)

		for j in range(1,self.h + 1):
			for i in range(1,self.w + 1):
				self.label = tk.Label(self,bg = self.backgroundColor,width = self.size,padx = 0,pady=0)
				self.label.grid(column = i,row = j)
				self.columnconfigure(i,pad = 0)
				self.rowconfigure(i,pad = 0)
				self.squares[i][j] = self.label

	def colorSquareSnake(self,x,y):
		self.squares[x][y].config(bg = self.snakeColor)
		self.dataSquares[x][y] = 1

	def colorSquareBackground(self,x,y):
		self.squares[x][y].config(bg = self.backgroundColor)
		self.dataSquares[x][y] = 0

	def keyPressHandler(self,event):
		
		if (event.keycode == 37): #Left
			if (self.direction % 2 == 1):
				self.direction = 0
		elif (event.keycode == 38): #Up
			if (self.direction % 2 == 0):
				self.direction = 1
		elif (event.keycode == 39): #Right
			if (self.direction % 2 == 1):
				self.direction = 2
		elif (event.keycode == 40): #Down
			if (self.direction % 2 == 0):
				self.direction = 3
	def move(self):
		if (self.direction == 0): #Left
			self.colorSquareBackground(self.xpos,self.ypos)
			self.xpos = self.xpos - 1
			self.colorSquareSnake(self.xpos,self.ypos)
		elif (self.direction == 1): #Up
			self.colorSquareBackground(self.xpos,self.ypos)
			self.ypos = self.ypos - 1
			self.colorSquareSnake(self.xpos,self.ypos)
		elif (self.direction == 2): #Right
			self.colorSquareBackground(self.xpos,self.ypos)
			self.xpos = self.xpos + 1
			self.colorSquareSnake(self.xpos,self.ypos)
		elif (self.direction == 3): #Down
			self.colorSquareBackground(self.xpos,self.ypos)
			self.ypos = self.ypos + 1
			self.colorSquareSnake(self.xpos,self.ypos)

speed = 1



app = Application()

def task():
	app.move()
	app.after(200,task)

app.master.title('Snake')

app.after(200,task)
app.mainloop()