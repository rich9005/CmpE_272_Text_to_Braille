import MySQLdb
db = MySQLdb.connect("localhost","root","fallcon2015","python123")
cursor = db.cursor()
cursor.execute("SELECT * from temp;")
data = cursor.fetchall()
print (data)
#print "Database version : %s " % data
db.close()