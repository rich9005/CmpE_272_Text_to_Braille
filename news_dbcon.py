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
print 'hi'
#print article.summary

for x in article.text.encode("utf-8").split("|"):
#	try:
		y = x
		cursor.execute("insert into news(news_data) values (%s)",[(y)])
		print ("Hi---",y)
		db.commit()
#	except:
#		db.rollback()


#print article.text.encode("utf-8")
article.download()
article.html
#article.parse()
#print article.text
#bbc_article.download()
#bbc_article.parse()
#bbc_article.nlp()