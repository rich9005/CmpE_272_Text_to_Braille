from django.shortcuts import render_to_response
from django.http import HttpResponse
import MySQLdb
import re
import socket


no = 1
bno = 35
book_title = 0
url_ip = socket.gethostbyname(socket.gethostname())
db = MySQLdb.connect("localhost","root","fallcon2015","python123")
cursor = db.cursor()
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
#	try:


print ("======================")

cursor.execute("select news_data from news1 where news_id =(%s)", [no])
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
def clickNext(request,row_id):
	if request.POST.get('click', True):
		no = int(row_id)
		global url_ip
		no +=  1 
		no = str(no)
		cursor.execute("select news_data from news1 where news_id =(%s)", [no])
		rows = cursor.fetchall()
		rowss = re.sub(r'\W+', ' ', str(rows))
		#return HttpResponse("abc")
		image_array = textToBraille(rowss)
		print ("=====================================hrichrichrichNEXTheheheh==============================")
		#print rowss
		return render_to_response("story/home.html", {'hello': rowss, 'bye' : image_array, 'hey' : url_ip,'row_id' : no})
		#home()


def clickPrevious(request, row_id):
	if request.POST.get('click', True):
		no = int(row_id)
		global url_ip
		if no >=2 :
			no -=  1 
			no = str(no)
			cursor.execute("select news_data from news1 where news_id =(%s)", [no])
			rows = cursor.fetchall()
			rowss = re.sub(r'\W+', ' ', str(rows))
			#return HttpResponse("abc")
			image_array = textToBraille(rowss)
			print ("=====================================richrichrihPREVPREV==============================")
			#print rowss
			return render_to_response("story/home.html", {'hello': rowss, 'bye' : image_array, 'hey' : url_ip ,'row_id' : no})
		else :
			rowss = " No more Previous news Press next "
			image_array = textToBraille(rowss)
			return render_to_response("story/home.html", {'hello': rowss, 'bye' : image_array, 'hey' : url_ip ,'row_id' : no})

def clickNextBook(request,bnop,book_id):
	if request.POST.get('click', True):
		bno = int(bnop)
		bno +=  1 
		book_title = book_id
		if book_title == "1":
			book_page = "Huckelberry Finn (" +url_ip+ ")" 
		else:
			book_page = "The Mad King (" +url_ip+ ")"
		cursor.execute("select text from books where pageNumber =(%s) and bookId =(%s)", (bno,book_title))
		rows = cursor.fetchall()
		rowss = re.sub(r'\W+', ' ', str(rows))
		#return HttpResponse("abc")
		image_array = textToBraille(rowss)
		print ("=====================================hrichrichrichNEXTheheheh==============================")
		#print rowss
		return render_to_response("story/books.html", {'hello': rowss, 'bye' : image_array, 'hey' : book_page, 'pgno' : bno, 'book_idd' : book_title})
		#home()


def clickPreviousBook(request,bno,book_id):
	if request.POST.get('click', True):
		bno = int(bno)
		bno -=  1
		book_title = book_id
		if book_title == "1":
			book_page = "Huckelberry Finn (" +url_ip+ ")"
		else:
			book_page = "The Mad King (" +url_ip+ ")"
		cursor.execute("select text from books where pageNumber =(%s) and bookId =(%s)", (bno,book_title))
		rows = cursor.fetchall()
		rowss = re.sub(r'\W+', ' ', str(rows))
		#return HttpResponse("abc")
		image_array = textToBraille(rowss)
		print ("=====================================richrichrihPREVPREV==============================")
		#print rowss
		return render_to_response("story/books.html", {'hello': rowss, 'bye' : image_array, 'hey' : book_page, 'pgno' : bno, 'book_idd' : book_title})
		
def clickBooks(request,book_id):
	if request.POST.get('click', True):
		global bno
		
		bno -=  1 
		book_title = book_id
		global book_title 
		if book_title == "1":
			book_page = "Huckelberry Finn"
		else:
			book_page = "The Mad King"

		cursor.execute("select text from books where pageNumber =(%s)and bookId =(%s)", (bno,book_title))
		rows = cursor.fetchall()
		rowss = re.sub(r'\W+', ' ', str(rows))
		#return HttpResponse("abc")
		image_array = textToBraille(rowss)
		print ("=====================================richrichrihPREVPREV==============================")
		#print rowss
		return render_to_response("story/books.html", {'hello': rowss, 'bye' : image_array, 'hey' : book_page , 'pgno' : bno , 'book_idd' : book_id})

def home(request):
	global no
	global url_ip
	cursor.execute("select news_data from news1 where news_id =(%s)", [no])
	rows = cursor.fetchall()
	rowss = re.sub(r'\W+', ' ', str(rows))
	image_array = textToBraille(rowss)
	return render_to_response("story/home.html", {'hello': rowss, 'bye' : image_array, 'hey' : url_ip ,'row_id' : no})


