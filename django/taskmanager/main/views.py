from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/main page.html')

def about(request):
    return HttpResponse('<h4>Hello World</h4>')

def index_css(request):
    return render(request, 'main/gmain.css')