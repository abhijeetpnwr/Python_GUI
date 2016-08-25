# Pull down menu are attached to a parent menu (using add_cascade), instead of a toplevel window.

from Tkinter import *

root = Tk()

def hello():
    print "hello!"

def save():
	print "Ohk"

# create a toplevel menu
menubar = Menu(root)

pulldownmwnu = Menu(menubar)

pulldownmwnu.add_command(label="open", command=hello)
pulldownmwnu.add_command(label="save!", command=save)

menubar.add_cascade(label="file",menu=pulldownmwnu)

# display the menu
root.config(menu=menubar)


toolbar = Frame(root,bg="blue")
toolbar.pack(side=TOP,fill=X)

copybtn = Button(toolbar,text="copy icon")
copybtn.pack(side=LEFT,padx=10,pady=10)

pastebtn = Button(toolbar,text="paste icon")
pastebtn.pack(side=LEFT,padx=10,pady=10)

root.mainloop()