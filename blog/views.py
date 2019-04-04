from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	# return HttpResponse('About')
	return render(request,'about.html')

def home(request):
	return render(request,'home.html')
