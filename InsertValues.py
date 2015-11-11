import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","jaisrikrishna28","dbase")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO DB(ID, STRING) 

         VALUES ('1', 'All recent U.S. military veterans and their families will now be offered in-state tuition rates to public colleges and universities throughout the country, the White House said on Wednesday.')"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()

except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
