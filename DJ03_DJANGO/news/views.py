from django.shortcuts import render
from .models import News_Posts

def home(request):
    news = News_Posts.objects.all()
    return render(request, template_name= 'news/news.html', context={'news': news})


