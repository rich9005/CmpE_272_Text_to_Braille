#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","shruthi123","dbase" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
results=[]

sql="SELECT STRING FROM DB where ID='1'" 
        
try:
   # Execute the SQL command
   cursor.execute(sql)

   # Fetch the row in a list of lists.
   results.extend(cursor.fetchone())
   
   d=[''] 
   d.extend(results)
   print d
   print results

   for i in results:
    print i[1:30]
    final=i[1:30]

   for k in final:
    print k 

except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()




































































































































































