import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...


q = "CREATE TABLE students (name TEXT, id INTEGER)"

fObj = open("peeps.csv") 
d=csv.DictReader(fObj)
c.execute(q)    #run SQL query

for k in d:
    q = "INSERT INTO students VALUES ('"+k["name"]+"', "+k["id"]+")"
    print q
    c.execute(q)



q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
c.execute(q)
fObj = open("courses.csv")
d=csv.DictReader(fObj)
c.execute(q)    #run SQL query        

for k in d:
    q = "INSERT INTO courses VALUES ('"+k["name"]+"', "+k["id"]+", "+k["mark"]+")"
    c.execute(q)


#==========================================================
db.commit() #save changes
db.close()  #close database


