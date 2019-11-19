import sqlite3
conn = sqlite3.connect('training.db')
c=conn.cursor()
ss=input('enter search roll no:')
cs=input('enter search Course no:')
es=input('enter search emp no:')

c.execute("SELECT ROLLNO, NAME, REGDNO, ADDRESS from STUDENT where ROLLNO=?",(ss))
for row in c:
	print ("ROLLNO = ", row[0])
	print ("NAME = ", row[1])
	print ("REGDNO = ", row[2])
	print ("ADDRESS = ", row[3], "\n")

c.execute("SELECT COURSENO, COURSENAME, PRICE, DESCRIPTION from COURSE where COURSENO=?",(cs))
for row in c:
	print ("COURSENO = ", row[0])
	print ("COURSENAME = ", row[1])
	print ("PRICE = ", row[2])
	print ("DESCRIPTION = ", row[3], "\n")

c.execute("SELECT EMPNO, ENAME, AGE, ADDRESS from EMPLOYEE where EMPNO=?",(es))
for row in c:
	print ("EMPNO = ", row[0])
	print ("ENAME = ", row[1])
	print ("AGE = ", row[2])
	print ("ADDRESS = ", row[3], "\n")

conn.close()

