
import tkinter
from tkinter import *
from tkinter import filedialog as fd
import shutil
import os


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('File Transfer Machine')
        self.master.config(bg='lightgray')

        self.btnSource = Button(self.master, text='Browse Files to Select', width=20, height=2, command=self.browse)
        self.btnSource.grid(row=0, column=1,padx=(10,10),pady=(20,10), sticky=E)
        
        # Creates entry widget for source path to be stored in
        self.sourceEntry = Entry(self.master,text='',font=("Helvetica", 16), fg='black', bg='lightblue')
        self.sourceEntry.grid(row=1, column=1,padx=(30,0),pady=(30,0))

        self.btnDestination = Button(self.master, text='Choose Destination', width=20, height=2, command=self.destination)
        self.btnDestination.grid(row=2, column=1,padx=(10,10),pady=(20,10), sticky=E)
        
        # Creates entry widget for dest path to be stored in
        self.desEntry = Entry(self.master,text='',font=("Helvetica", 16), fg='black', bg='lightblue')
        self.desEntry.grid(row=3, column=1,padx=(30,0),pady=(30,0))

        self.btnCancel = Button(self.master, text='Cancel', width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=4, column=0,padx=(100,10),pady=(100,0), sticky=SW)

        self.btnCopy = Button(self.master, text='Copy File', width=10, height=2, command=self.copy)
        self.btnCopy.grid(row=4, column=2,padx=(10,10),pady=(100,0), sticky=SW)

        
    def browse(self):
        srcPath = fd.askdirectory() # Allows user to select directory when called
        self.sourceEntry.delete(0, END) 
        self.sourceEntry.insert(END, srcPath) # Stores chosen directory in entry box
        
    def destination(self) :
        srcPath = fd.askdirectory() # Allows user to select directory when called
        self.desEntry.delete(0, END)
        self.desEntry.insert(END, srcPath) # Stores chosen directory in entry box

    def copy(self) :
        #set where the source of the files are
        source = self.sourceEntry.get()
        fileList = os.listdir()
        #set the destination path
        destination = self.desEntry.get()
        # we are saying move the files to thier new destination
        shutil.move(source, destination)
        
    def cancel(self) :
        self.master.destroy()
    

        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
