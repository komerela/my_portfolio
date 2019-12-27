from django.shortcuts import render
from django.views.generic import TemplateView


"""
Create view for index file
"""

def index(request):
	name = 'home'
	context = {'foo': 'bar'}
	return render(None, 'port/index.html', context)

class WelcomeView(TemplateView):
	    template_name = "port/index.html"
