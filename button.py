from tkinter import *

file1 = open("MyFile.txt","r")
lines = file1.readlines()
lineArray = []
for line in lines:
    lineArray.append(line)

window=Tk()
entry1 = Entry(window, bd = 5, bg='red')
Lb1 = Listbox(window, bg='pink',  bd=4)
for i in range(len(lineArray)):
    Lb1.insert(i, lineArray[i])
# variable = entry1.get()

def openNewWindow(tex_t):
    windowNew = Tk()
    variable = entry1.get()
    print (type(variable))
    print ("hey")
    labelNew = Label(windowNew, text = tex_t, bg='red')
    print (variable)
    entryNew = Entry(windowNew, bd = 5, bg='blue')
    #variable = entryNew.get()
    btn= Button(windowNew, text="Click here to open a new window", fg='blue', bg='red', command = lambda: openNewWindow(entryNew.get()))
    btn.place(x=90, y=100)
    windowNew.geometry("300x200+10+10")
    windowNew.title('Hello Python New Window')
    labelNew.place(x=60, y=50)
    labelNew.pack()
    entryNew.place(x=75, y=80)
    entryNew.pack()
    windowNew.mainloop()

btn=Button(window, text="Click here to open a new window", fg='blue', bg='red', command = lambda: openNewWindow(entry1.get()))
btn.place(x=80, y=100)
window.title('Hello Python')
entry1.place(x=60, y=50)
entry1.pack()
Lb1.place(x=110, y=170)
# scrollbar = Scrollbar(Lb1, orient="vertical")
# scrollbar.config(command=Lb1.yview)
# scrollbar.pack(side=RIGHT,fill=Y)
# Lb1.config(yscrollcommand=scrollbar.set)
Lb1.pack()
window.geometry("700x500+10+10")
window.mainloop()
