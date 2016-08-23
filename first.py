
# A blank window with a label

from Tkinter import *

root = Tk() #A blank constructor , creates a simple window 

topFrame = Frame(root) #Created a Frame
topFrame.pack() # Pack frame in window

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM) # Packing bottom Frame 

button = Button(bottomFrame,text="Sart Blast",fg="purple")
button.pack()


thelabel = Label(root,text="Blast++ Wrapper Tutorial") #created a label

thelabel.pack() # It means just pack all widgest into window , putting widget to root table 

root.mainloop() #  To continuously  keep showing window