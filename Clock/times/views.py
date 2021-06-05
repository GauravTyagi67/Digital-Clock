from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
	now=datetime.now()
	format='%H:%M:%S %p'
	current_time=now.strftime(format)
	current_date=now.strftime('%d-%m-%Y')
	context={'time':current_time,'date':current_date}
	return render(request,"clock.html",context)