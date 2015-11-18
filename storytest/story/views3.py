from django.shortcuts import render_to_response
from django.http import HttpResponse
from newspaper import Article
import MySQLdb
import re

no = 22
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
#print article.summary
#y = "<center><h2>Top News</h2></center><table border=1>"
#start1 = "<tr><td>"
#start2 = "</td><td>"
#i = 1
#end = "</td></tr>"
#z = " "
#for x in article.text.encode("utf-8").split("|"):
#		if (x != " "):
#			start = start1 + str(i)+ start2
#			z +=  start + x  + end  
#			i = i + 1
#abc = y + z
#print (abc)
for x in article.text.encode("utf-8").split("|"):
#	try:
		y = x
		cursor.execute("insert into news(news_data) values (%s)",[y])
		#print ("Hi---",y)
		db.commit()


print ("======================")

cursor.execute("select news_data from news where news_id =(%s)", [no])
rows = cursor.fetchall()
rowss = re.sub(r'\W+', ' ', str(rows))
print rowss

testStr = " "
rows_array  = rowss.split()
for word in rows_array:
	for c in word:
		c_lower = c.lower()
		tc = "/static/braille-alphabet-flashcard-"+c_lower+".jpg"
		print tc
		testStr += tc + " "
	testStr += "/static/braille-alphabet-flashcard-space.jpg" + " "
print (testStr)



#rowss_value = "Test braille values"
#image_string = "/static/a_br.jpg /static/b_br.jpg"
def textToBraille(rowss):
	testStr = " "
	rows_array  = rowss.split()
	for word in rows_array:
		for c in word:
			c_lower = c.lower()
			tc = "/static/braille-alphabet-flashcard-"+c_lower+".jpg"
			#print tc
			testStr += tc + " "
		testStr += "/static/braille-alphabet-flashcard-space.jpg" + " "

	image_string = testStr
	image_array = image_string.split()
	print(image_array)
	return image_array
#def home(request):
#	return HttpResponse("Hello world!")
# Create your views here.
	#for x in article.text.encode("utf-8").split("|"):
	#	z +=  start + x  + end  
	#	print (y) 
	#print ("Hey ya'all ")
	#x = "<table> <tr><td>1</td><td>thisi is one</td></tr><tr><td>2</td><td>this is two</td></tr>"
	#abc = y + z
#	return HttpResponse(abc)
def clickNext(request):
	if request.POST.get('click', True):
		global no
		global url
		no +=  1 
		cursor.execute("select news_data from news where news_id =(%s)", [no])
		rows = cursor.fetchall()
		rowss = re.sub(r'\W+', ' ', str(rows))
		#return HttpResponse("abc")
		image_array = textToBraille(rowss)
		print ("=====================================hrichrichrichNEXTheheheh==============================")
		#print rowss
		return render_to_response("story/home.html", {'hello': rowss, 'bye' : image_array, 'hey' : url})
		#home()


def clickPrevious(request):
	if request.POST.get('click', True):
		global no
		global url
		no -=  1 
		cursor.execute("select news_data from news where news_id =(%s)", [no])
		rows = cursor.fetchall()
		rowss = re.sub(r'\W+', ' ', str(rows))
		#return HttpResponse("abc")
		image_array = textToBraille(rowss)
		print ("=====================================richrichrihPREVPREV==============================")
		#print rowss
		return render_to_response("story/home.html", {'hello': rowss, 'bye' : image_array, 'hey' : url})

def clickNextBook(request):
	if request.POST.get('click', True):
		global no
		global url
		no +=  1 
		cursor.execute("select news_data from news where news_id =(%s)", [no])
		rows = cursor.fetchall()
		rowss = re.sub(r'\W+', ' ', str(rows))
		#return HttpResponse("abc")
		image_array = textToBraille(rowss)
		print ("=====================================hrichrichrichNEXTheheheh==============================")
		#print rowss
		return render_to_response("story/books.html", {'hello': rowss, 'bye' : image_array, 'hey' : url})
		#home()


def clickPreviousBook(request):
	if request.POST.get('click', True):
		global no
		global url
		no -=  1 
		cursor.execute("select news_data from news where news_id =(%s)", [no])
		rows = cursor.fetchall()
		rowss = re.sub(r'\W+', ' ', str(rows))
		#return HttpResponse("abc")
		image_array = textToBraille(rowss)
		print ("=====================================richrichrihPREVPREV==============================")
		#print rowss
		return render_to_response("story/books.html", {'hello': rowss, 'bye' : image_array, 'hey' : url})
		
def clickBooks(request):
	if request.POST.get('click', True):
		global no
		book_title = "Huckelberry Finn"
		no -=  1 
		cursor.execute("select news_data from news where news_id =(%s)", [no])
		rows = cursor.fetchall()
		rowss = re.sub(r'\W+', ' ', str(rows))
		#return HttpResponse("abc")
		image_array = textToBraille(rowss)
		print ("=====================================richrichrihPREVPREV==============================")
		#print rowss
		return render_to_response("story/books.html", {'hello': rowss, 'bye' : image_array, 'hey' : book_title})

def home(request):
	global no
	global url
	cursor.execute("select news_data from news where news_id =(%s)", [no])
	rows = cursor.fetchall()
	rowss = re.sub(r'\W+', ' ', str(rows))
	image_array = textToBraille(rowss)
	return render_to_response("story/home.html", {'hello': rowss, 'bye' : image_array, 'hey' : url })


