import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","shruthi123","dbase" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
results=[]
sql="SELECT STRING FROM DB" 
        
try:
   # Execute the SQL command
   cursor.execute(sql)
   
   

   # Fetch the row in a list of lists.
   results.extend(cursor.fetchone())
    
   d=[''] 
   d.extend(results)
    
   print d
   print results
   
   
   for index in range(len(results)):


    print 'current results:', results[index].split() 

    z=results[index].split() 
    print z[:6]

    v=z[:6]

    print v

   for col in v:
    col[:100]
    finals=col[:100]

    for cols in list(col):
     print cols

except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()





































