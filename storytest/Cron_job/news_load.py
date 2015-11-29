from newspaper import Article
import MySQLdb

url = u'http://timesofindia.indiatimes.com/world/us'

db = MySQLdb.connect("localhost","root","fallcon2015","python123")
cursor = db.cursor()
article = Article(url)
article.download()
article.html
article.parse()
x = article.authors
print x
print (url)
i = 1
for x in article.text.encode("utf-8").split("|"):
                y = x
                if y.isspace() or len(y) > 100 :
                        print ("null")
                else :
                        print (len(y))
                        print y
                        cursor.execute("update news1 set news_data = (%s) where news_id =(%s)",[y , i])
                        db.commit()
                        i += 1
