import sqlite3
from tkinter import *
def ViewStudentDetails():
    i=5
    window = Toplevel(top)
    con=sqlite3.connect('training.db')
    cursor = con.cursor()
    window.title("Student Details")
    message=cursor.execute('SELECT ROLLNO, NAME, REGDNO, ADDRESS from STUDENT')#write database query
    #message = cursor.fetchall()
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Roll No").grid(row=3,column=0)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Student Name").grid(row=3,column=1)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Registraton No").grid(row=3,column=2)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Address").grid(row=3,column=3)
    for roll,name,reg,add in message :
        Label(window,text=roll).grid(row=i,column=0)
        Label(window,text=name).grid(row=i,column=1)
        Label(window,text=reg).grid(row=i,column=2)
        Label(window,text=add).grid(row=i,column=3)
        i=i+1
    #Label(window,bg='yellow2',font=('Lucida Bright',20),height=10,width=90, text=message).pack()
    #con.commit()
    #con.close()



def notice():
    window = Toplevel(top)
    Label(window, bg='white',font=('Lucida Calligraphy',20),height=10,width=50,text="tomorrow is class test \n you have to come with your admit card").pack()




def viewCourseDetails():
    i=5
    window = Toplevel(top)
    window.title("Course Details")
    con=sqlite3.connect('training.db')
    cursor = con.cursor()
    window.title("Course Details")
    message=cursor.execute('SELECT COURSENO, COURSENAME, PRICE, DESCRIPTION from COURSE')# DB QUERY
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Course No").grid(row=3,column=0)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Course Name").grid(row=3,column=1)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="price").grid(row=3,column=2)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Description").grid(row=3,column=3)
    for roll,name,reg,add in message :
        Label(window,text=roll).grid(row=i,column=0)
        Label(window,text=name).grid(row=i,column=1)
        Label(window,text=reg).grid(row=i,column=2)
        Label(window,text=add).grid(row=i,column=3)
        i=i+1
    #message = cursor.fetchall()
    #Label(window,bg='yellow2',font=('Lucida Bright',20),height=10,width=90, text=message).pack()
    #con.commit()
    #con.close()

def ViewEmployeeDetails():
    i=5
    window = Toplevel(top)
    window.title("Employee Details")
    con=sqlite3.connect('training.db')
    cursor = con.cursor()
    message=cursor.execute('SELECT EMPNO, ENAME, AGE, ADDRESS from EMPLOYEE')
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Course No").grid(row=3,column=0)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Course Name").grid(row=3,column=1)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="price").grid(row=3,column=2)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Description").grid(row=3,column=3)
    for roll,name,reg,add in message :
        Label(window,text=roll).grid(row=i,column=0)
        Label(window,text=name).grid(row=i,column=1)
        Label(window,text=reg).grid(row=i,column=2)
        Label(window,text=add).grid(row=i,column=3)
        i=i+1
    #message = cursor.fetchall()
    #Label(window,bg='yellow2',font=('Lucida Bright',20),height=10,width=90, text=message).pack()
    #con.commit()
    #con.close()

def addStudentDetails():
    con=sqlite3.connect('training.db')
    cursor = con.cursor()
    r2=e2.get()
    r3=e3.get()
    r4=e4.get()
    r5=e5.get()
    cursor.execute("INSERT INTO STUDENT (ROLLNO,NAME,REGDNO,ADDRESS) VALUES (?,?,?,?)",(r2,r3,r4,r5));
    con.commit()
    con.close()

def addCourse():
    con=sqlite3.connect('training.db')
    cursor = con.cursor()
    '''cp=int(input('enter courseno:'))
    cn=str(input('enter coursename:'))
    p=int(input('enter price:'))
    d=str(input('enter description:'))'''
    r2=e2.get()
    r3=e3.get()
    r4=e4.get()
    r5=e5.get()
    cursor.execute("INSERT INTO COURSE (COURSENO,COURSENAME,PRICE,DESCRIPTION) VALUES (?,?,?,?)",(r2,r3,r4,r5));
    con.commit()
    con.close()

def addEmp():
    con=sqlite3.connect('training.db')
    cursor = con.cursor()
    '''e=int(input('enter empno:'))
    en=str(input('enter empname:'))
    ag=int(input('enter age:'))
    ad=str(input('enter address:'))'''
    r2=e2.get()
    r3=e3.get()
    r4=e4.get()
    r5=e5.get()
    cursor.execute("INSERT INTO EMPLOYEE (EMPNO,ENAME,AGE,ADDRESS) VALUES (?,?,?,?)",(r2,r3,r4,r5));
    con.commit()
    con.close()

def newWindows():
    window = Toplevel(top)
    window.title("Search Here")
    ssl=Label(window,text='Search Here',fg="indian red2",font=('copper black',16))
    ssl.grid(row=4,column=1)
    ##ssl.config(width=30,height=1)
    sse=Entry(window)
    sse.grid(row=4,column=2)
    print(sse.get())
    ssb=Button(window,text='Search',bd=4,font=('georgia',16),bg='cyan2',command=lambda:studSearch(sse.get()))
    ssb.grid(row=6,column=2)

def newWindowe():
    window = Toplevel(top)
    window.title("Search Here")
    ssl=Label(window,text='Search Here',fg="indian red2",font=('copper black',16))
    ssl.grid(row=4,column=1)
    ##ssl.config(width=30,height=1)
    sse=Entry(window)
    sse.grid(row=4,column=2)
    print(sse.get())
    ssb=Button(window,text='Search',bd=4,font=('georgia',16),bg='cyan2',command=lambda:empSearch(sse.get()))
    ssb.grid(row=6,column=2)

def newWindowc():
    window = Toplevel(top)
    window.title("Search Here")
    ssl=Label(window,text='Search Here',fg="indian red2",font=('copper black',16))
    ssl.grid(row=4,column=1)
    ##ssl.config(width=30,height=1)
    sse=Entry(window)
    sse.grid(row=4,column=2)
    print(sse.get())
    ssb=Button(window,text='Search',bd=4,font=('georgia',16),bg='cyan2',command=lambda:courseSearch(sse.get()))
    ssb.grid(row=6,column=2)

def studSearch(a):
    i=5
    ##print(a)
    con=sqlite3.connect('training.db')
    cursor = con.cursor()
    window = Toplevel(top)
    window.title("Student Result")
    ##ssr=input('enter search roll no:')
    ##ssr=sse.get()
    message=cursor.execute("SELECT ROLLNO, NAME, REGDNO, ADDRESS from STUDENT where ROLLNO=?",(a))
    '''for row in cursor:
        print ("ROLLNO = ", row[0])
        print ("NAME = ", row[1])
        print ("REGDNO = ", row[2])
        print ("ADDRESS = ", row[3], "\n")'''
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Roll No").grid(row=3,column=0)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Student Name").grid(row=3,column=1)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Registraton No").grid(row=3,column=2)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Address").grid(row=3,column=3)
    for roll,name,reg,add in message :
        Label(window,text=roll).grid(row=i,column=0)
        Label(window,text=name).grid(row=i,column=1)
        Label(window,text=reg).grid(row=i,column=2)
        Label(window,text=add).grid(row=i,column=3)
        i=i+1
    ##Label(window,bg='yellow2',font=('Lucida Bright',20),height=10,width=90, text=message).pack()
    con.commit()
    con.close()

def empSearch(a):
    i=5
    con=sqlite3.connect('training.db')
    cursor = con.cursor()
    window = Toplevel(top)
    window.title("Employee Search")
    ##es=input('enter search emp no:')
    message=cursor.execute("SELECT EMPNO, ENAME, AGE, ADDRESS from EMPLOYEE where EMPNO=?",(a))
    '''for row in cursor:
        print ("EMPNO = ", row[0])
        print ("ENAME = ", row[1])
        print ("AGE = ", row[2])
        print ("ADDRESS = ", row[3], "\n")'''
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="EMP No").grid(row=3,column=0)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Employee Name").grid(row=3,column=1)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Age").grid(row=3,column=2)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Address").grid(row=3,column=3)
    for roll,name,reg,add in message :
        Label(window,text=roll).grid(row=i,column=0)
        Label(window,text=name).grid(row=i,column=1)
        Label(window,text=reg).grid(row=i,column=2)
        Label(window,text=add).grid(row=i,column=3)
        i=i+1
    con.commit()
    con.close()

def courseSearch(a):
    i=5
    con=sqlite3.connect('training.db')
    cursor = con.cursor()
    window = Toplevel(top)
    window.title("Student Search")
    ##cs=input('enter search course no:')
    message=cursor.execute("SELECT COURSENO, COURSENAME, PRICE, DESCRIPTION from COURSE where COURSENO=?",(a))
    '''for row in cursor:
        print ("COURSENO = ", row[0])
        print ("COURSENAME = ", row[1])
        print ("PRICE = ", row[2])
        print ("DESCRIPTION = ", row[3],"\n")'''
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Course No").grid(row=3,column=0)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Course Name").grid(row=3,column=1)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Price").grid(row=3,column=2)
    Label(window,bg='yellow2',font=('Lucida Bright',20),text="Description").grid(row=3,column=3)
    for roll,name,reg,add in message :
        Label(window,text=roll).grid(row=i,column=0)
        Label(window,text=name).grid(row=i,column=1)
        Label(window,text=reg).grid(row=i,column=2)
        Label(window,text=add).grid(row=i,column=3)
        i=i+1
    con.commit()
    con.close()

def newWindowsu():
    window = Toplevel(top)
    window.title("Update Here")
    ssl1=Label(window,text='rollno',fg="indian red2",font=('copper black',16))
    ssl1.grid(row=4,column=1)
    sse1=Entry(window)
    sse1.grid(row=4,column=2)
    ssl2=Label(window,text='address',fg="indian red2",font=('copper black',16))
    ssl2.grid(row=5,column=1)
    sse2=Entry(window)
    sse2.grid(row=5,column=2)
    #print(sse1.get())
    #print(sse2.get())
    ssb=Button(window,text='Update',bd=4,font=('georgia',16),bg='cyan2',command=lambda:studentUpdate(int(sse1.get()),sse2.get()))
    ssb.grid(row=6,column=2)

def newWindoweu():
    window = Toplevel(top)
    window.title("Update Here")
    ssl1=Label(window,text='empno',fg="indian red2",font=('copper black',16))
    ssl1.grid(row=4,column=1)
    sse1=Entry(window)
    sse1.grid(row=4,column=2)
    ssl2=Label(window,text='address',fg="indian red2",font=('copper black',16))
    ssl2.grid(row=5,column=1)
    sse2=Entry(window)
    sse2.grid(row=5,column=2)
    #print(sse.get())
    ssb=Button(window,text='Update',bd=4,font=('georgia',16),bg='cyan2',command=lambda:employeeUpdate(int(sse1.get()),sse2.get()))
    ssb.grid(row=6,column=2)

def newWindowcu():
    window = Toplevel(top)
    window.title("Update Here")
    ssl1=Label(window,text='Courseno',fg="indian red2",font=('copper black',16))
    ssl1.grid(row=4,column=1)
    sse1=Entry(window)
    sse1.grid(row=4,column=2)
    ssl2=Label(window,text='Price',fg="indian red2",font=('copper black',16))
    ssl2.grid(row=5,column=1)
    sse2=Entry(window)
    sse2.grid(row=5,column=2)
    #print(sse1.get())
    #print(sse2.get())
    ssb=Button(window,text='Update',bd=4,font=('georgia',16),bg='cyan2',command=lambda:courseUpdate(sse1.get(),sse2.get()))
    ssb.grid(row=6,column=2)

def studentUpdate(r,ua):
    conn=sqlite3.connect('training.db')
    c=conn.cursor()
    #r=int(input("please enter the roll no."))
    #ua=str(input('enter new value of address'))
    conn.execute("UPDATE STUDENT SET ADDRESS='%s' WHERE ROLLNO==%d" % (ua,r))
    print('updated successfully student')
    conn.commit()

def employeeUpdate(e,ea):
    conn=sqlite3.connect('training.db')
    c=conn.cursor()
    #e=int(input("please enter the empno no."))
    #ea=str(input('enter new value of address'))
    conn.execute("UPDATE EMPLOYEE SET ADDRESS='%s' WHERE EMPNO==%d" % (ea,e))
    print('updated successfully employee')
    conn.commit()

def courseUpdate(co,p):
    conn=sqlite3.connect('training.db')
    c=conn.cursor()
    #c=int(input("please enter the course no."))
    #de=str(input('enter new value of description'))
    print(co,p)
    conn.execute("UPDATE COURSE SET PRICE==%d WHERE COURSENO==%d" % (int(p),int(co)))
    print('updated successfully course')
    conn.commit()

def clear():
    e2.delete(0,'end')
    e3.delete(0,'end')
    e4.delete(0,'end')
    e5.delete(0,'end')

top=Tk()
top.title(' DESKTOP TRAINING SYSTEM')
top.configure(background='powder blue')


'''
T1=Frame(top,width=400,height=1600,bg="BLUE",relief=SUNKEN)
T1.pack(side=TOP)

T=Frame(top,width=600,height=700,bg="blue",relief=SUNKEN)
T.pack(side=)
f1=Frame(top,width=300,height=700,bg="yellow",relief=SUNKEN)
f1.pack(side=LEFT)
f2=Frame(top,width=400,height=700,bg="WHITE",relief=SUNKEN)
f2.pack(side=RIGHT)
'''
label=Label(top,text='Training Management System',fg='blue',font=('algerian',50))
label.grid(row=0,column=1)

b1=Button(top,padx=5,pady=5,bd=8,text='Student details',font=('Algerian',12),command=ViewStudentDetails,bg='yellow')
b1.grid(row=1,column=0)
b1.config(width=15,height=1)
b2=Button(top,padx=5,pady=5,bd=8,text='Course details ',font=('Algerian',12),command=viewCourseDetails,bg='yellow')
b2.grid(row=2,column=0)
b2.config(width=15,height=1)

b3=Button(top,padx=5,pady=5,bd=8,text='Employee details ',font=('Algerian',12),command=ViewEmployeeDetails,bg='yellow')
b3.grid(row=3,column=0)
b3.config(width=15,height=1)

b4=Button(top,padx=5,pady=5,bd=8,text='Add Student ',font=('Algerian',12),command=addStudentDetails,bg='yellow')
b4.grid(row=4,column=0)
b4.config(width=15,height=1)

b5=Button(top,padx=5,pady=5,bd=8,text='Add course ',font=('Algerian',12),command=addCourse,bg='yellow')
b5.grid(row=5,column=0)
b5.config(width=15,height=1)
b6=Button(top,padx=5,pady=5,bd=8,text='Add Employee ',font=('Algerian',12),command=addEmp,bg='yellow')
b6.grid(row=6,column=0)

b6.config(width=15,height=1)
b7=Button(top,padx=5,pady=5,bd=8,text='Student search ',font=('Algerian',12),command=newWindows,bg='yellow')
b7.grid(row=7,column=0)
b7.config(width=15,height=1)
b8=Button(top,padx=5,pady=5,bd=8,text='Employee search ',font=('Algerian',12),command=newWindowe,bg='yellow')
b8.grid(row=8,column=0)
b8.config(width=15,height=1)
b9=Button(top,padx=5,pady=5,bd=8,text='Course search ',font=('Algerian',12),command=newWindowc,bg='yellow')
b9.grid(row=9,column=0)
b9.config(width=15,height=1)

b10=Button(top,padx=5,pady=5,bd=8,text='Update Student ',font=('Algerian',12),command= newWindowsu,bg='yellow')
b10.grid(row=10,column=0)
b10.config(width=15,height=1)

b11=Button(top,padx=5,pady=5,bd=8,text='Update Employee ',font=('Algerian',12),command= newWindoweu,bg='yellow')
b11.grid(row=11,column=0)
b11.config(width=15,height=1)

b12=Button(top,padx=5,pady=5,bd=8,text='Update Course ',font=('Algerian',12),command=newWindowcu,bg='yellow')
b12.grid(row=12,column=0)
b12.config(width=15,height=1)


l1=Label(top,text='ENTER DETAILS TO REGISTER  COURSE:-',fg='deep pink',font=('copper black',16))
l1.grid(row=1,column=1)

l2=Label(top,text='Roll/course/employee No:',fg="indian red2",font=('copper black',16))
l2.grid(row=2,column=1)
l2.config(width=30,height=1)
courseUpdate
e2=Entry(top,bg='light sky blue',font=('copper black',10))
e2.grid(row=2,column=2)
r2=e2.get()

l3=Label(top,text='Student/Course/Employee Name:',fg="indian red2",font=('copper black',16))
l3.grid(row=3,column=1)
l3.config(width=30,height=1)

e3=Entry(top,bg='light sky blue',font=('copper black',10))
e3.grid(row=3,column=2)
r3=e3.get()

l4=Label(top,text='REGD,NO/Price/age:',fg="indian red2",font=('copper black',16))
l4.grid(row=4,column=1)
l4.config(width=30,height=1)

e4=Entry(top,bg='light sky blue',font=('copper black',10))
e4.grid(row=4,column=2)
r4=e4.get()

l5=Label(top,text='ADDRESS/Description',fg="indian red",font=('copper black',16))
l5.grid(row=5,column=1)
l5.config(width=30,height=1)

e5=Entry(top,bg='light sky blue',font=('copper black',10))
e5.grid(row=5,column=2)
r5=e5.get()

b10=Button(top,text='clear',bd=4,font=('georgia',16),bg='cyan2',command=clear)
b10.grid(row=6,column=2)
b11=Button(top,text='NOTICE',bd=8,width=10,font=('georgia',16),bg='GREEN2',command=notice)
b11.grid(row=8,column=1)



top.mainloop()
