import mysql.connector


## code to convert text file in to a dictionary wiht key as page number and value as the 5 text lines
with open("C:/Users/neeraj/Desktop/272Project/Huckleberry.txt") as f:
    content = f.read().splitlines()
dict={1:"Start"}
i=0
j=1
for l in content:
    s=str(dict.get(j))
    s="".join(e for e in s if (e.isspace()or e.isalpha()or e.isdigit()))

    l="".join(e for e in str(l) if (e.isspace()or e.isalpha()or e.isdigit()))
    s=s+l
    dict.update({j:s[0:]})

    i=i+1
    if(i==5):
       i=0
       j=j+1
## Code for  storing data from dictionary to database

cnx = mysql.connector.connect(user='root', password='Caradigm123',
                              host='localhost',
                              database='272projectbook')

cursor = cnx.cursor()
for k,v in dict.iteritems():
  query = "INSERT INTO book2(bookId,pageNumber,text) " \
            "VALUES(%s,%s,%s)"
  args = (1,k,v[4:])

  cursor.execute(query,args)

cnx.commit()
cursor.close()
cnx.close()








