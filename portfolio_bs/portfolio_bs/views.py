from django.shortcuts import render


"""
Create view for index file
"""

def index(request):
	name = 'home'
	return render(request, 'port/index.html',)