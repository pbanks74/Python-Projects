#   Python  Ver:    3.9.2
#
#   Author:             Paul D. Fairbanks
#
#   Purpose:          Phonebook demo. Demonstrating OOP, Tkinter GUI module,
#                             using Tkinter parent and child relationships.
#
#   Tested OS:      This code was written and tested to work with Windows 10 and MacOS Big Sur 11.4
#
####################################################################################

from tkinter import *
import tkinter as tk
from tkinter import messagebox
#other modules imported to have access to:
import phonebook_gui
import phonebook_func


# Frame is the tkinter frame class that the created class will inherit from
class ParentWindow(Frame) :
    def __init__(self, master, *args, **kwargs) :
        Frame.__init__(self, master, *args, **kwargs)

        # Defines master config:
        self.master = master
        self.master.minsize(500,300) # (height,width)
        self.master.maxsize(500,300)
        # CenterWindow method centers app on user's screen:
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="F0F0F0")
        # Built-in Tkinter protocol method to catch if user clicks upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Loading GUI widgets from a sperate module to keep code comparmentalized and clutter free
        phonebook_gui.load_gui(self)


if __name__ == "__main__" :
    root = tk.Tk() # Creates window
    App = ParentWindow(root) # Passes in our class
    root.mainloop() # Created a loop so the window does not go away immediately 
        
