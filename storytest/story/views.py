from django.shortcuts import render_to_response
from django.http import HttpResponse

def home(request):
#	return HttpResponse("Hello world!")
# Create your views here.
	print ("Hey ya'all ")
	return render_to_response("story/home.html", {'hello': "Hello Variable!"})