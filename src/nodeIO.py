from tkinter import *
import sys

def window(disptxt):
    root = Tk()
    frame = Frame(root)
    frame.pack()

    bottomframe = Frame(root)
    bottomframe.pack( side = BOTTOM )

    message = Label(frame, text=disptxt)
    message.pack( side = LEFT)

    root.mainloop()
