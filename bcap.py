import os
import configparser
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk



class Window:
	def __init__(self):
		self.root = tk.Tk()
		# self.root.geometry("1320x800")
		self.root.title("BEER CAP ANALYSIS PROGRAM")

		self.frame = tk.Frame(self.root)
		self.frame.grid(row=0)


		## MAIN FRAME
		self.frameMain = tk.Frame(self.frame)
		self.frameMain.grid(row=0, column=0, columnspan=2)

		tempNames = os.listdir('templates/')
		tempPics = [Image.open('templates/'+path) for path in tempNames]
		# tempPics = [np.resize(img, (100,100)) for img in tempPics]
		tempPics = [ImageTk.PhotoImage(img) for img in tempPics]

		tempNames = [name.split('.')[0] for name in tempNames]
		tempNames = [name.replace('_', ' ') for name in tempNames]

		rows = 4
		columns = 2

		self.plusbuttons = []
		self.minusbuttons = []
		self.labels = []
		self.pictures = []
		self.counters = []

		for column in range(columns):
			for row in range(rows):
				print(row, column, tempNames[column*rows+row])

				nr = column*rows+row
				button = tk.Button(self.frameMain, text='-', font="Times 80 bold", width=3, height=2, command= lambda nr=nr: self.minus(nr))
				button.grid(row=row, column=column*5, padx=10)#, sticky='W')
				self.minusbuttons.append(button)

				label = tk.Label(self.frameMain, text=tempNames[column*rows + row], font="Times 30 bold")
				label.grid(row=row, column=column*5+1)
				self.labels.append(label)

				label = tk.Label(self.frameMain, text='Biersorte', width=300)
				label.grid(row=row, column=column*5+2)
				label.configure(image=tempPics[column*rows + row])
				self.pictures.append(label)

				variable = tk.StringVar()
				label = tk.Label(self.frameMain, textvariable=variable, font="Times 30 bold", width=3)
				label.grid(row=row, column=column*5+3)
				self.counters.append(variable)
				self.counters[-1].set("0")

				nr = column*rows+row
				button = tk.Button(self.frameMain, text='+', font="Times 80 bold", width=3, height=2, command= lambda nr=nr: self.plus(nr))
				button.grid(row=row, column=column*5+4, padx=10)#, sticky='W')
				self.plusbuttons.append(button)


		tk.Button(self.frame, text='Neues Bier einpflegen', font="Times 30 bold", height=2, command=self.newBeer).grid(row=1, column=0, pady=20)
		tk.Button(self.frame, text='Alle Biere anzeigen', font="Times 30 bold", height=2, command=self.showList).grid(row=1, column=1, pady=20)



        ## SETTINGS FRAME
		self.frameSettings = tk.Frame(self.frame)
		self.frameSettings.grid(row=0, column=0, columnspan=2)
		self.info = self.frameSettings.grid_info()
		self.frameSettings.grid_forget()

		tk.Text(self.frameSettings, height=1, width=50).grid(row=0)
		tk.Button(self.frameSettings, text="speichern", command=self.close).grid(row=1)


		self.root.mainloop()


	def close(self):
		self.info = self.frameSettings.grid_info()
		self.frameSettings.grid_forget()

	def plus(self, nr):
		print("PLUS AT",nr)
		count = int(self.counters[nr].get())
		self.counters[nr].set(str(count + 1))


	def minus(self, nr):
		print("MINUS AT", nr)
		count = int(self.counters[nr].get())
		self.counters[nr].set(str(count - 1))

	def newBeer(self):
		print("WUHUUU NEW BEER")
		self.frameSettings.grid(self.info)

	def showList(self):
		print("SHOW LIST")
		self.info = self.frameSettings.grid_info()
		self.frameSettings.grid_forget()


x = Window()