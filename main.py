import mysql.connector as s
con = s.connect(host = "localhost", user = "root", password = "root", database = "Student_Tracker_System")
cur = con.cursor()
def todotable():
   try:
       cur.execute("create table Todo(Day date, Task varchar(100), Completion varchar(10))")
       print("Table Created")
   except:
       print("Table Exist")
       todoinsert()
      
def todoinsert():
   Day = input("Enter date in YYYY-MM-DD form: ")
   Task = input("Enter task in less than 100 words: ")
   Completion = input("Enter done or not done: ")
   query = "insert into ToDo values(%s,%s,%s)"
   rec = (Day, Task, Completion)
   cur.execute(query,rec)
   con.commit()
   print('Added Successfully')
  
def tododisplay():
   d = input("Enter date to display corresponding task in YYYY-MM-DD form: ")
   query = "select * from Todo where Day = %s"
   d1 = (d,)
   cur.execute(query,d1)
   data = cur.fetchall()
   for i in data:
     print(i)
 
def weeklytable():
   try:
       cur.execute("create table Weekly_Goals(Start_Day date, End_Day date, Task varchar(100), Completion varchar(10))")
       print("Table Created")
   except:
       print("Table Exists")
       weeklyinsert()
      
def weeklyinsert():
   Start_Day = input("Enter start date in YYYY-MM-DD form: ")
   End_Day = input("Enter end date in YYYY-MM-DD form: ")
   Task = input("Enter task in less than 100 words: ")
   Completion = input ("Enter done or not done: ")
   query = "insert into Weekly_Goals values(%s,%s,%s,%s)"
   rec = (Start_Day, End_Day, Task, Completion)
   cur.execute(query,rec)
   con.commit()
   print('Added Successfully')
  
def weeklydisplay():
   sd = input("Enter start date to display corresponding task in YYYY-MM-DD form: ")
   ed = input("Enter end date to display corresponding task in YYYY-MM-DD form: ")
   query = "select * from Weekly_Goals where Start_Day >= %s and End_Day <=%s"
   d1 = (sd,ed)
   cur.execute(query,d1)
   data = cur.fetchall()
   for i in data:
     print(i)
 
def monthlytable():
   try:
       cur.execute("create table Monthly_Goals(Month varchar(15) Primary key, Goals varchar(100))")
       print("Table Created")
   except:
       print("Table Exists")
       monthlyinsert()
      
def monthlyinsert():
   m = input("Enter the month: ")
   g = input("Enter the goal of the month in less than 100 words: ")
   query = "insert into Monthly_Goals values('%s','%s')"
   rec =(m,g)
   cur.execute(query,rec)
   con.commit()
   print('Added Successfully')
  
def monthlydisplay():
   d = input("Enter date to display corresponding task in YYYY-MM-DD form: ")
   query="select * from Monthly_Goals where month = '%s'"
   d1=(d,)
   cur.execute(query,d1)
   data = cur.fetchall()
   for i in data:
       print(i)
 
def dicttable():
   try:
       cur.execute("create table Dictionary(Word varchar(50), Meaning varchar(200))")
       print("Table Created")
   except:
       print("Table Exists")
       dictinsert()
      
def dictinsert():
   w = input('Enter the new word: ')
   m = input('Enter the meaning of the new word: ')
   Rec = (w, m)
   Cmd = "insert into Dictionary values(%s,%s)"
   cur.execute(Cmd,Rec)
   con.commit()
   print('Added Successfully')
   
def dictdisplay():
   try:
       w = input('Enter the word to search: ')
       cur.execute("select Meaning from Dictionary where Word = '%s'" %(w,))
       data = cur.fetchone()
       for i in data:
           print(i)
   except:
       print('Error Found')
 
def sem1table():
   try:
       cur.execute("create table Semester1(Subject varchar(30), Syllabus varchar(100))")
       print("Table Created")
   except:
       print("Table Exist")
       sem1insert()
      
def sem2table():
   try:
       cur.execute("create table Semester2(Subject varchar(30), Syllabus varchar(100))")
       print("Table Created")
   except:
       print("Table Exist")
       sem2insert()
      
def sem3table():
   try:
       cur.execute("create table Semester3(Subject varchar(30), Syllabus varchar(100))")
       print("Table Created")
   except:
           print("Table Exist")
           sem3insert()
          
def sem1insert():
   Sub1 = input("Enter the subject: ")
   Syl1 = input("Enter the syllabus in less than 100 words: ")
   query = "insert into Semester1 values(%s,%s)"
   rec = (Sub1,Syl1)
   cur.execute(query,rec)
   con.commit()
   print('Added Successfully')
  
def sem2insert():
   Sub2 = input("Enter the subject: ")
   Syl2 = input("Enter the syllabus in less than 100 words: ")
   query = "insert into Semester2 values(%s,%s)"
   rec = (Sub2,Syl2)
   cur.execute(query,rec)
   con.commit()
   print('Added Successfully')
  
def sem3insert():
   Sub3 = input("Enter the subject: ")
   Syl3 = input("Enter the syllabus in less than 100 words: ")
   query = "insert into Semester3 values(%s,%s)"
   rec = (Sub3,Syl3)
   cur.execute(query,rec)
   con.commit()
   print('Added Successfully')
  
def sem1display():
   d = input("Enter the subject: ")
   query = "select * from Semester1 where Subject = %s"
   d1 = (d,)
   cur.execute(query,d1)
   data = cur.fetchall()
   for i in data:
       print(i)
      
def sem2display():
   d = input("Enter the subject: ")
   query = "select * from Semester2 where Subject = %s"
   d1 = (d,)
   cur.execute(query,d1)
   data = cur.fetchall()
   for i in data:
       print(i)
      
def sem3display():
   d = input("Enter the subject: ")
   query = "select * from Semester3 where Subject = %s"
   d1 = (d,)
   cur.execute(query,d1)
   data = cur.fetchall()
   for i in data:
       print(i)
 
def booktable():
   try:
       cur.execute("create table Reading_List(Day date, Bookname varchar(100), Liked_or_Disliked varchar(10))")
       print("Table Created")
   except:
       print("Table Exists")
       bookinsert()
      
def bookinsert():
   Day = input("Enter date in YYYY-MM-DD form: ")
   Bookname = input("Enter name of the Book: ")
   Liked_or_Disliked = input("Enter liked or disliked: ")
   query = "insert into Reading_List values(%s,%s,%s)"
   rec = (Day, Bookname, Liked_or_Disliked)
   cur.execute(query,rec)
   con.commit()
   print('Added Successfully')
  
def bookdisplay():
   d = input("Enter date to display corresponding task in YYYY-MM-DD form: ")
   query = "select * from Reading_List where Day = %s"
   d1=(d,)
   cur.execute(query,d1)
   data = cur.fetchall()
   for i in data:
       print(i)
 
print('************************* Welcome to Student Tracker System *************************')
print()
print('''Menu:
Type 1 - To Do List
Type 2 - Weekly Goals
Type 3 - Monthly Goals
Type 4 - Dictionary
Type 5 - Semester Wise Syllabus
Type 6 - Reading List
Type 7 - Exit''')
print()


while True:
    q = int(input('Enter the number as per your choice: '))
    while True:
        if q == 1:
            print('''Sub Menu:
Type 1 - To Create Table
Type 2 - To Insert Values
Type 3 - To Display Values
Type 4 - To Exit''')
            t = int(input("Enter the number as per your choice: "))
            if t == 1:
                todotable()
            elif t == 2:
                todoinsert()
            elif t == 3:
                tododisplay()
            elif t == 4:
                print('Bye')
                break
            else:
                print('Error Found')
                con.commit()
        elif q == 2:
            print('''Sub Menu:
Type 1 - To Create Table
Type 2 - To Insert Values
Type 3 - To Display Values
Type 4 - To Exit''')
            w = int(input("Enter the number as per your choice: "))
            if w == 1:
                weeklytable()
            elif w == 2:
                weeklyinsert()
            elif w == 3:
                weeklydisplay()
            elif w == 4:
                print('Bye')
                break
            else:
                print('Error Found')
                con.commit()
        elif q == 3:
            print('''Sub Menu:
Type 1 - To Create Table
Type 2 - To Insert Values
Type 3 - To Display Values
Type 4 - To Exit''')
            m = int(input("Enter the number as per your choice: "))
            if m == 1:
                monthlytable()
            elif m == 2:
                monthlyinsert()
            elif m == 3:
                monthlydisplay()
            elif m == 4:
                print('Bye')
                break
            else:
                print('Error Found')
                con.commit()
        elif q == 4:
            print('''Sub Menu:
Type 1 - To Create Table
Type 2 - To Insert Values
Type 3 - To Display Values
Type 4 - To Exit''')
            dic = int(input("Enter the number as per your choice: "))
            if dic == 1:
                dicttable()
            elif dic == 2:
                dictinsert()
            elif dic == 3:
                dictdisplay()
            elif dic == 4:
                print('Bye')
                break
            else:
                print('Error Found')
                con.commit()
        elif q == 5:
            print('''Sub Menu:
Type 1 - To Create Table
Type 2 - To Insert Values
Type 3 - To Display Values
Type 4 - To Exit''')
            n = int(input('Enter the number of the semester: '))
            if n == 1:
                s1 = int(input('Enter the number as per your choice: '))
                if s1 == 1:
                    sem1table()
                elif s1 == 2:
                    sem1insert()
                elif s1 == 3:
                    sem1display()
                elif s1 == 4:
                    print('Bye')
                    break
                else:
                    print('Error Found')
            elif n == 2:
                s2 = int(input('Enter the number as per your choice: '))
                if s2 == 1:
                    sem2table()
                elif s2 == 2:
                    sem2insert()
                elif s2 == 3:
                    sem2display()
                elif s2 == 4:
                    print('Bye')
                    break
                else:
                    print('Error Found')
            elif n == 3:
                s3 = int(input('Enter the number as per your choice: '))
                if s3 == 1:
                    sem3table()
                elif s3 == 2:
                    sem3insert()
                elif s3 == 3:
                    sem3display()
                elif s1 == 4:
                    print('Bye')
                    break
                else:
                    print('Error Found')
            else:
                print('Error Found')
                con.commit()
        elif q == 6:
            print('''Sub Menu:
Type 1 - To Create Table
Type 2 - To Insert Values
Type 3 - To Display Values
Type 4 - To Exit''')
            b = int(input("Enter the number as per your choice: "))
            if b == 1:
                booktable()
            elif b == 2:
                bookinsert()
            elif b == 3:
                bookdisplay()
            elif b == 4:
                print('Bye')
                break
            else:
                print('Error Found')
                con.commit()
        else:
            print('Error Found')  
print('Bye!')
