from tkinter import *
from data import records


class AddRecordDialogBuilder:
    def __init__(self):
        pass
        
    
    def addRecord(self):
        '''Build a dialog that takes name,age,salary
        from the user and adds up to a temp. data structure
        '''

        root = Tk()

        self.entries = []
        fields = ('name ','age   ','salary')
        for field in fields:
            row = Frame(root)

            label = Label(row,text=field)
            label.config(font=('Ariel',10,'bold'))
            entry = Entry(row)

            label.pack(side='left',padx=5)
            entry.pack(side='right',padx=5)
            row.pack()
            self.entries.append(entry)
            
        row = Frame(root)
        addButton = Button(row,text="Add Record",command=self.save)
        addButton.pack(side='left',padx=5)

        cancelButton = Button(row,text="Cancel",command=root.destroy)
        cancelButton.pack(side='right',padx=5)

        row.pack(padx=5,pady=5)

    def save(self):
        name = self.entries[0].get()
        age = self.entries[1].get()
        salary = self.entries[2].get()

        records[name] = {'age':age,'salary':salary}
        self.show()

    def show(self):
        print(records)

        
class Persistance:
    def saveToFile(self):
        fobj = open("records.txt","w")
        for name in records:
            age = records[name]['age']
            salary = records[name]['salary']
            fobj.write(name+" ")
            fobj.write(age+" ")
            fobj.write(salary+" ")
            fobj.write("\n")
            
#we are building the class MenuBuilder
            
class MenuBuilder:
    def __init__(self):

        try:
            fobj = open("records.txt","r")
            for line in fobj:
                fields = line.split()
                name = fields[0]
                age = fields[1]
                salary = fields[2]

                records[name] = {'age':age,'salary':salary}
        except:
            pass

        top = Tk()

        menubar = Menu()
        
        menu = Menu(menubar)

        #add menu items
        # command chaining doing two things in one line
        #a1 = AddrecordDialogBuilder() - creating object
        #a1.addRecord() 
        menu.add_command(label="Add Record",command=AddRecordDialogBuilder().addRecord)
        menu.add_command(label="Edit Record",command=top.destroy)
        menu.add_command(label="Delete Record",command=top.destroy)
        menu.add_command(label="Quit",command=Persistance().saveToFile)

        #add to menubar
        menubar.add_cascade(label="Records",menu=menu)

        menu = Menu(menubar)
        menu.add_command(label="I am helpless",command=top.destroy)
        menubar.add_cascade(label="Help",menu=menu)

        top['menu'] = menubar   

        top.mainloop()

MenuBuilder()
