from Tkinter import *

class drawButtons:
	def __init__(self,master):
		print "Need to initialize drawbuttons"

		frame=Frame(master)
		frame.pack()

		self.button_submit = Button(frame,text="Start Blast",fg="purple",command=self.printMessage)
		self.button_submit.pack()
		

	def printMessage(self):
		print "It should start doing Blast"

root=Tk()
dw = drawButtons(root)
root.mainloop()