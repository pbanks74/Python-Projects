
import sqlite3 #imports module
conn = sqlite3.connect('academy.db') #creates a database named 'academy'
with conn: #while connected do the following code
    cur = conn.cursor() #creates shortcut by shortening variable
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fileName STRING)") #creates table with 2 columns
    conn.commit() #saves the SQL statement

conn = sqlite3.connect('academy.db')

#tuple of file names
files_tuple = ('information.docx', 'Hello.txt', 'myImage.png', \
               'myMovie.mpg', 'World.txt','data.pdf', 'myPhoto.jpg')


#loop through each object in the tuple to find the filenames that end in ".txt"
for x in files_tuple:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        #inserts files chosen by parameters into table
            cur.execute("INSERT INTO tbl_files (col_fileName) Values (?)", (x,))
            print(x) #prints to screen
conn.close() #closes connection to avoid data leak
            


               






