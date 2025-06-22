from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("test", views.test, name="test"),
    path("contact", views.contact, name="contact"),
]

