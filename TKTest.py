__author__ = 'Administrator'

# from Tkinter import *
#
# from FileDialog import *
#
# root = Tk()
#
# fd = LoadFileDialog(root)
#
# filename = fd.go()
#
# print filename
#
# root.mainloop()

import tkFileDialog

filename = tkFileDialog.askdirectory(title ="Select Directory", initialdir = 'D:/Python')

print filename