import os
from tkinter import filedialog
from tkinter import *
import fasttext

root = Tk()
path = StringVar()

def browse_button():
    global path
    global filename
    filename = filedialog.askdirectory()
    path.set(filename)
    print(filename)

def retrieve_input():
    input = self.e1.get("1.0",END)
    print(input)

# r=root, d=directories, f = files
def search(path):
    files = []
    print(path)
    for r, d, f in os.walk(path):
        for file in f:
            #files.append(os.path.join(r, file)) #directory + file
            files.append( file + "\n")
    file1 = open("text.txt", "w")
    for f in files:
        file1.writelines(f)
    file1.close()
    model = fasttext.train_unsupervised("text.txt", model='skipgram')

    print(model.words)  # list of words in dictionary
    print(model['ana'])  # get the vector of the work



e1 = Text(master=root)
#e1.insert(0, 'keyword')
e1.grid(row=0, columnspan=4)
lbl1 = Label(master=root,textvariable=path)
lbl1.grid(row=2, column=1)
button2 = Button(text="Browse", command=browse_button)
button2.grid(row=2, column=3)
button1 = Button(text="Search", command= lambda: search(filename))
button1.grid(row=4, columnspan=4)

mainloop()