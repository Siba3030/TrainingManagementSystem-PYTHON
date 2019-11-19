import sqlite3
conn = sqlite3.connect('training.db')
c=conn.cursor()
r=int(input('enter rollno:'))
n=str(input('enter name:'))
re=int(input('enter registration number:'))
a=str(input('enter address:'))
cp=int(input('enter courseno:'))
cn=str(input('enter coursename:'))
p=int(input('enter price:'))
d=str(input('enter description:'))
e=int(input('enter empno:'))
en=str(input('enter empname:'))
ag=int(input('enter age:'))
ad=str(input('enter address:'))
cid=int(input('enter serialno:'))
crsid=int(input('enter courseid:'))
emid=int(input('enter employeeid:'))
sdid=int(input('enter studentid:'))

c.execute("INSERT INTO STUDENT(ROLLNO,NAME,REGDNO,ADDRESS) VALUES (?,?,?,?)",(r,n,re,a));
c.execute("INSERT INTO COURSE(COURSENO,COURSENAME,PRICE,DESCRIPTION) VALUES (?,?,?,?)",(cp,cn,p,d));
c.execute("INSERT INTO EMPLOYEE(EMPNO,ENAME,AGE,ADDRESS) VALUES (?,?,?,?)",(e,en,ag,ad));
c.execute("INSERT INTO COURSE_EMPLOYEE_reg(CEID,COURSEID,EMPLOYEEID) VALUES (?,?,?)",(cid,crsid,emid));
c.execute("INSERT INTO COURSE_STD_reg(CSID,COURSEID,STUDENTID) VALUES (?,?,?)",(cid,crsid,sdid));
conn.commit()

c.execute("SELECT ROLLNO, NAME, REGDNO, ADDRESS from STUDENT")
for row in c:
	print ("ROLLNO = ", row[0])
	print ("NAME = ", row[1])
	print ("REGDNO = ", row[2])
	print ("ADDRESS = ", row[3], "\n")

c.execute("SELECT COURSENO, COURSENAME, PRICE, DESCRIPTION from COURSE")
for row in c:
	print ("COURSENO = ", row[0])
	print ("COURSENAME = ", row[1])
	print ("PRICE = ", row[2])
	print ("DESCRIPTION = ", row[3], "\n")

c.execute("SELECT EMPNO, ENAME, AGE, ADDRESS from EMPLOYEE")
for row in c:
	print ("EMPNO = ", row[0])
	print ("ENAME = ", row[1])
	print ("AGE = ", row[2])
	print ("ADDRESS = ", row[3], "\n")
conn.close()
