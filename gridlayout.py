
# A blank window with a label

from Tkinter import *

def leftClick(event):
	print "Left button Clicked"

def rightClick(event):
	print "right button clicked"

root = Tk() #A blank constructor , creates a simple window 

frame = Frame(root,height=600,width=400)

frame.bind("<Button-1>",leftClick)

frame.bind("<Button-3>",rightClick)  #Button-2 is for middle mouse button

frame.pack()

root.mainloop()


