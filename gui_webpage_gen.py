
import tkinter
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 300))
        self.master.title('Webpage Generator')
        self.master.config(bg='lightgray')

        self.lblText = Label(self.master,text='Enter Text: ',font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblText.grid(row=0, column=0,padx=(30,0),pady=(30,0))

        self.txtEntry = Entry(self.master,text='{}',font=("Helvetica", 16), fg='black', bg='white')
        self.txtEntry.grid(row=0, column=1,padx=(30,0),pady=(30,0))

        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=3, column=2,padx=(0,0),pady=(30,0), sticky=SW)

        self.btnCancel = Button(self.master, text='Cancel', width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=3, column=1,padx=(0,100),pady=(30,0), sticky=SW)



    def submit(self) : # defines submit button
        f = open("webpage_generator.html", "w")    # Creates file if doesn't exist
        f.write(self.txtEntry.get())   # Sets user input as the body of the webpage 
        f.close()                                                                  

        webbrowser.open_new_tab("webpage_generator.html") # Opens webpage in new browser tab

       
    def cancel(self) : #defines cancel button
        self.master.destroy() #closes gui




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
