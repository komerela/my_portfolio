from django.shortcuts import render



"""
Create view for index file
"""

def index(request):
	name = 'home'
	context = {'foo': 'bar'}
	return render(None, 'port/index.html', context)