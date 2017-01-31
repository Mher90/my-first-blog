from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse("<h1>Hello World</h1>")

def post_list(request):
    return render(request, 'blog/post_list.html', {})
