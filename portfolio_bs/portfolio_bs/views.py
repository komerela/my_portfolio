from django.shortcuts import render
from django.template.context import RequestContext


"""
Create view for index file
"""

def index(request):
	name = 'home'
	return render(request, 'port/index.html', context_instance=RequestContext(request))