import MySQLdb



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

cnx = MySQLdb.connect('localhost','root','root'
                              ,'272projectbook')

cursor = cnx.cursor()
global pagenumber
pagenumber=1

for k,v in dict.iteritems():
  query = "INSERT INTO book6(bookId,pageNumber,text) " \
            "VALUES(%s,%s,%s)"
  f=4
  l=0
  x=0
  print(v.__len__())
  while(x < v.__len__()/100):
   if(v.__len__()%100==0):
    s=v[f:l+100]
    args = (1,pagenumber,s)
    cursor.execute(query,args)
    pagenumber=pagenumber+1
    f=f+100
    l=l+100
    x=x+1
   elif(v.__len__()%100 < 100):
    s=v[f:v.__len__()]
    args = (1,pagenumber,s)
    cursor.execute(query,args)
    pagenumber=pagenumber+1
    f=f+100
    l=l+100
    x=x+1

cnx.commit()
cursor.close()
cnx.close()





































































































