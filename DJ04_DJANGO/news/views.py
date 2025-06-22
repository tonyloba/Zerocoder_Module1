from django.shortcuts import render, redirect
from .models import News_Posts
from .forms import News_Posts_Form

def home(request):
    news = News_Posts.objects.all()
    return render(request, template_name= 'news/news.html', context={'news': news})

def add_new_news(request):
    errors = ''
    if request.method == 'POST':
        form = News_Posts_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:news_home')
        else:
            errors = form.errors

    form = News_Posts_Form(request.POST or None)
    return render(request, template_name= 'news/add_news.html', context={'form': form, 'errors': errors})


