
# A blank window with a label

from Tkinter import *



def doBlast():
	print "Should do Blast stuff"

root = Tk() #A blank constructor , creates a simple window 

Label1 = Label(root,text="Enter Username")

Label2  = Label(root,text="Enter Password")

entry_1 = Entry(root,text="Enter username")

entry_2 = Entry(root,text="Enter password")

c = Checkbutton(root,text="Keep me logged in")

button_blast = Button(root,text = "Do Blast",command=doBlast)

Label1.grid(row=0, sticky=E) # Put in  1st row , 1st column  , sticly  makes it ticl to east

Label2.grid(row=1)

entry_1.grid(row=0,column=1)

entry_2.grid(row=1,column=1)

c.grid(columnspan=2)

button_blast.grid(row=3)

root.mainloop()

