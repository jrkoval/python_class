from tkinter import *

def compute():
    p = int(entry1.get())
    r = int(entry2.get())
    t = int(entry3.get())

    result = p * r * t/100
#because label4 has __setitem__ we can do
    label4['text'] = str(result)

def clear():
    entry1.delete(0,'end')
    entry2.delete(0,'end')
    entry3.delete(0,'end')
    label4['text'] = " "
    entry1.focus_set()

root = Tk()

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)

f1.pack()
f2.pack()
f3.pack()
f4.pack()
f5.pack()

#now add visible widgets
#label box
label1 = Label(f1, text="Principal")
label1.config(font=('ariel',10,'bold'))
label1.pack(side='left')
#enry box
entry1 = Entry(f1)
entry1.pack
entry1.pack(side='right',padx=10, pady=10)

label2 = Label(f2, text="Rate")
label2.config(font=('ariel',10,'bold'))
label2.pack(side='left')
#enry box
entry2 = Entry(f2)
entry2.pack(side='right',padx=10, pady=10)

label3 = Label(f3, text="Time")
label3.config(font=('ariel',10,'bold'))
label3.pack(side='left')
#enry box
entry3 = Entry(f3)
entry3.pack(side='right',padx=10, pady=10)

label4 = Label(f4, text="Result")
label4.config(font=('ariel',10,'bold'))
label4.pack(side='left')

#enry box
entry4 = Entry(f4)
entry4.pack(side='right',padx=10, pady=10)

button1 = Button(f5,text="Compute",command=compute)
button1.pack(side='left',padx=10,pady=10)
button2=Button(f5,text="Clear",command=clear)


button2.pack(side='left',padx=10,pady=10)
entry1.focus_set()
root.mainloop()
