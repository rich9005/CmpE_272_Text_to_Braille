import MySQLdb

with open("C:/Users/neeraj/Desktop/272Project/Huckleberry.txt") as f:
    content = f.read().splitlines()
dict={1:"Start"}
i=0
j=1
k=""
for l in content:
    s=str(dict.get(j))
    s="".join(e for e in s if (e.isspace()or e.isalpha()or e.isdigit()))

    l="".join(e for e in str(l) if (e.isspace()or e.isalpha()or e.isdigit()))
    s=s+l
    k=k+l
    dict.update({j:s[0:]})

    i=i+1
    if(i==5):
       i=0
       j=j+1
## Code for  storing data from dictionary to database
cnx = MySQLdb.connect('localhost','root','root'
                              ,'272projectbook')

cursor = cnx.cursor()
global pagenumber
pagenumber=1

query = "INSERT INTO book8(bookId,pageNumber,text) " \
            "VALUES(%s,%s,%s)"
m=0
n=100
q=k.__len__()/100
for t in range(0,q+1):
   s=k[m:n]
   m=m+100
   n=n+100
   args = (1,pagenumber,s)
   cursor.execute(query,args)
   pagenumber=pagenumber+1

cnx.commit()
cursor.close()
cnx.close()





































































































