import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

q ="SELECT name, mark FROM students, courses WHERE courses.id=students.id"
newc = db.execute(q)
r2 = {}
d2 = {}
for record in newc:
    if record[0] not in r2.keys():
        r2[record[0]] = record[1]
        d2[record[0]] = 1
    else:
        r2[record[0]] += record[1]
        d2[record[0]] +=1
for a in r2.keys():
    r2[a]/=d2[a]
    print a
    print r2[a]

    
        
        
        

