from tkinter import *

#creating a frame for my window
class Application(Frame):
	"""My window application"""
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.varApple = IntVar()
		self.varBanana = IntVar()
		self.varMango = IntVar()
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		menubar = Menu(self)
		filemenu = Menu(menubar)
		filemenu.add_command(label='Convert', command=self.convert)
		filemenu.add_command(label='Clear', command=self.clear)
		filemenu.add_cascade(label='File', menu=filemenu)
		menubar.add_command(label='Quit', command=root.quit)
		root.config(menu=menubar)
		self.label1 = Label(self, text='Welcome to my window') #label widget
		self.label1.grid(row=0, column=0, sticky=W)
		self.button1 = Button(self, text='click me!', command=self.display) #button widget
		self.button1.grid(row=0, column=2, sticky=W)
		self.label2 = Label(self, text="what's your favorite fruit:")
		self.label2.grid(row=2, column=0, sticky=W)
		self.appleCheckButton = Checkbutton(self, text='apple', variable=self.varApple) #Checkbutton Widget
		self.appleCheckButton.grid(row=3, column=1, sticky=W)
		self.bananaCheckButton = Checkbutton(self, text='banana', variable=self.varBanana)
		self.bananaCheckButton.grid(row=4, column=1, sticky=W)
		self.mangoCheckButton = Checkbutton(self, text='mango', variable=self.varMango)
		self.mangoCheckButton.grid(row=5, column=1, sticky=W)
		self.submitFruit = Button(self, text='Tell us!', command=self.favoriteFruit)
		self.submitFruit.grid(row=6, column=1, sticky=W)
		self.label3 = Label(self, text="Tell us your name")
		self.label3.grid(row=7, column=0, sticky=W)
		self.name = Entry(self) #Enrty widget
		self.name.grid(row=8) 
		self.name.focus_set() #focus on the field whith a cursor
		self.buttonName = Button(self, text="Submit name", command=self.getName)
		self.buttonName.grid(row=9)
		self.label4 = Label(self, text="Tell us what you think about this class")
		self.label4.grid(row=10)
		self.userFeedback = Text(self, width=20, height=10) #Text widget for long lines of text
		self.userFeedback.grid(row=11, column=0, sticky=W)
		self.sendFeedback = Button(self, text="Submit Feedback!", command=self.getFeedback)
		self.sendFeedback.grid(row=12, column=0, sticky=W)
		self.opener = Button(self, text="open a new window", command=self.openWindow)
		self.opener.grid(row=13, column=0, sticky=W)
		



	def display(self):
		"""Event handler when clicked a button"""
		print('The button in the window was clicked!')

	def favoriteFruit(self):
		likeApple = self.varApple.get()
		likeBanana = self.varBanana.get()
		likeMango = self.varMango.get()
		if (likeApple):
			print("Your favorite fruit is Apple")

	def getName(self):
		user_name = self.name.get()
		self.name.delete(0, END)
		self.name.insert(END, "Your name is {username}".format(username=user_name))
		print("Your name is {username}".format(username=user_name))

	def getFeedback(self):
		user_feedback = self.userFeedback.get("1.0", END)
		self.userFeedback.delete("1.0", END)
		self.userFeedback.insert(END, "Thank you for your feedback!")
		print("The message was {userFeedback}".format(userFeedback=user_feedback))

	def openWindow(self):
		new = Tk()
		new.title("This is another window")

	def convert(self):
		pass

	def clear(self):
		pass


root = Tk()
root.title('This is a test window')
root.geometry('600x800')
app = Application(root)
app.mainloop()