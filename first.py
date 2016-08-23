
# A blank window with a label

from Tkinter import *

root = Tk() #A blank constructor , creates a simple window 

thelabel = Label(root,text="Blast++ Wrapper Tutorial") #created a label

thelabel.pack() # It means just pack all widgest into window , putting widget to root table 

root.mainloop() #  To continuously  keep showing window