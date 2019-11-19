import sqlite3
from tkinter import *
def View():
    window = Toplevel(top)
    con=sqlite3.connect('DATABASE NAME')
    cursor = con.cursor()
    cursor.execute('SELECT ')#write database query
    message = cursor.fetchall()
    Label(window, text=message).pack()
    con.commit()
    con.close()

def viewstudentDetails():
    window = Toplevel(top)
    con=sqlite3.connect('')
    cursor = con.cursor()
    cursor.execute('SELECT * from ')# DB QUERY
    message = cursor.fetchall()
    Label(window, text=message).pack()
    con.commit()
    con.close()

def ViewCoursedetails():
    window = Toplevel(top)
    con=sqlite3.connect('DATABASENAME')
    cursor = con.cursor()
    cursor.execute('SELECT * from ')
    message = cursor.fetchall()
    Message(window, text=message).pack()
    con.commit()
    con.close()
def SearchSTUDENT():
    window = Toplevel(top)
    con=sqlite3.connect('DB name')
    cursor = con.cursor()
    cursor.execute('SELECT')
    message = cursor.fetchall()
    Label(window, text=message).pack()
    con.commit()
    con.close()



def add():
    con=sqlite3.connect('DB NAME')
    cursor = con.cursor()
    rollno=e7.get()
    name=e2.get()
    dob=e3.get()
    cursor.execute("INSERT into  VALUES(?,?,?)",(e7,e2,e3))
    con.commit()
    con.close()#SAMPLE JUST HOW TO INSERT ADD MORE VALUES
                #BUT INSERT NOT WORKING ...

top=Tk()
top.title('STUDENT TRAINING SYSTEM')
top.configure(background='yellow')
label=Label(top,text=' WELCOME TO training',fg='blue',font=('algerian',30))
label.grid(row=0,column=1)

b1=Button(top,text='BUTTON NAME  ',font=('areial black',16),command='#function name',bg='blue')
b1.grid(row=1,column=0)

b2=Button(top,text=' ',font=('areial black',16),command= ' ',bg='blue')
b2.grid(row=2,column=0)

b3=Button(top,text=' ',font=('areial black',16),command=' ',bg='blue')
b3.grid(row=3,column=0)

b4=Button(top,text=' ',font=('areial black',16),command=' ',bg='blue')
b4.grid(row=4,column=0)

b5=Button(top,text=' ',font=('areial black',16),command=' ',bg='blue')
b5.grid(row=5,column=0)


l1=Label(top,text='ENTER DETAILS TO REGISTER  COURSE:-',font=('copper black',16))
l1.grid(row=1,column=1)

l2=Label(top,text='NAME:',font=('copper black',16))
l2.grid(row=2,column=1)
e2=Entry(top,font=('copper black',10))
e2.grid(row=2,column=2)

l3=Label(top,text='AGE:',font=('copper black',16))
l3.grid(row=3,column=1)
e3=Entry(top,font=('copper black',10))
e3.grid(row=3,column=2)

l4=Label(top,text='GENDER:',font=('copper black',16))
l4.grid(row=4,column=1)
e4=Entry(top,font=('copper black',10))
e4.grid(row=4,column=2)

l5=Label(top,text='COURSE',font=('copper black',16))
l5.grid(row=5,column=1)
e5=Entry(top,font=('copper black',10))
e5.grid(row=5,column=2)




b8=Button(top,text='SUBMIT->',font=('georgia',18),command=add)#ADD FUCTION UPARE LEKILU TO INSERT
b8.grid(row=6,column=2)

top.mainloop()


