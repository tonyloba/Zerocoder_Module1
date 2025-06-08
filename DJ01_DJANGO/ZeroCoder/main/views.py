from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    #return HttpResponse("Hello, world. You're at the main index.")
    return render(request, "index.html")

def new(request):
    #return HttpResponse("Hello, world. You're at the new.")
    return render(request, "new.html")

def test(request):
    #return HttpResponse("Hello, world. You're at the test.")
    return render(request, "test.html")