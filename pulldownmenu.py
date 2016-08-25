# Pull down menu are attached to a parent menu (using add_cascade), instead of a toplevel window.

from Tkinter import *

root = Tk()

def hello():
    print "hello!"

def save():
	print "Ohk I will save file later"

# create a toplevel menu
menubar = Menu(root)

pulldownmwnu = Menu(menubar)

pulldownmwnu.add_command(label="open", command=hello)
pulldownmwnu.add_command(label="save!", command=save)

menubar.add_cascade(label="file",menu=pulldownmwnu)

# display the menu
root.config(menu=menubar)

root.mainloop()