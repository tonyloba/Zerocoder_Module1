from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path("", views.home, name="news_home"),
    path("create_news", views.add_new_news, name="add_news_link"),

]