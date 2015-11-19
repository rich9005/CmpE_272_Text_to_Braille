__author__ = 'neeraj'
import glob, os
import mysql.connector

def createBookTabe():
 db = mysql.connector.connect(user='root', password='Caradigm123',
                              host='localhost',
                              database='272projectbook')
# prepare a cursor object using cursor() method
 cursor = db.cursor()
 s=0
 s1=cursor.execute("select max(bookId) from allbooks")
 data =cursor.fetchall()
 print(data)
 for row in data :
  s=row[0]+1
 db.commit()
# disconnect from server
 db.close()
 db = mysql.connector.connect(user='root', password='Caradigm123',
                              host='localhost',
                              database='272projectbook')
# prepare a cursor object using cursor() method
 cursor = db.cursor()
 cursor.execute("create table IF NOT EXISTS book"+str(s)+" (bookId int(11),pageNumber int(11),text varchar(1000));")

 query = "INSERT INTO allBooks(bookId,bookName) " \
            "VALUES(%s,%s)"
 args = (s,"newBook")

 cursor.execute(query,args)
 db.commit()
# disconnect from server
 db.close()
# set the directory path in path variable
path="C:/Users/neeraj/Desktop/desktopOld"
os.chdir(path)

# provide the file type , here we are taking text files
for file in glob.glob("*.txt"):
    bookPath=path+"/"+file
    print(bookPath)
#Load all boooks to database by calling book.py as method
