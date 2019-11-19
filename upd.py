try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter.ttk import *
    from tkinter import *
top=Tk()
top.title('NaaSClue')
top.configure(background='#141a3a')
import sqlite3
conn=sqlite3.connect('training.db')
c=conn.cursor()
i=int(input("please enter the roll no."))
ua=str(input('enter new value of address'))
conn.execute("UPDATE STUDENT SET ADDRESS='%s' WHERE ROLLNO==%d" % (ua,i))
print('updated succeddfully')
conn.commit()
class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('starttime', 'endtime', 'status')
        tv.heading("#0", text='Roll no.', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('starttime', text='Name')
        tv.column('starttime', anchor='center', width=100)
        tv.heading('endtime', text='egistrati')
        tv.column('endtime', anchor='center', width=100)
        tv.heading('status', text='Address')
        tv.column('status', anchor='center', width=100)
        tv.grid(sticky = (N,S,W,E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        result=conn.execute("select * from STUDENT ")
        for row in result:
            k1=row[0]
            k2=row[1]
            k3=row[2]
            k4=row[3]
            self.treeview.insert('', 'end', text=k2, values=(k1,k3, k4))
App(top)
top.mainloop()
