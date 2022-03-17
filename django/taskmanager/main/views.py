from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'main/templates/main/index.html')



def index_css(request):
    return render(request, 'main/templates/main/gmain.css')