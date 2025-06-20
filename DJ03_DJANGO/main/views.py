from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    #return HttpResponse("Hello, world. You're at the main index.")
    return render(request, "main/index.html" , context={'caption': 'Main Page Django'})

def new(request):
    #return HttpResponse("Hello, world. You're at the new.")
    return render(request, "main/new.html")

def test(request):
    #return HttpResponse("Hello, world. You're at the test.")
    return render(request, "main/test.html")

def contact(request):
    #return HttpResponse("Hello, world. You're at the contact.")
    return render(request, "main/contact.html")