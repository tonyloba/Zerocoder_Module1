from .models import News_Posts
from django import forms


class News_Posts_Form(forms.ModelForm):
    class Meta:
        model = News_Posts
        fields = ['title', 'short_info', 'text', 'publish_date', 'author']
        widgets = {
            'title': forms.Textarea(attrs={'rows': 1, 'class': 'form-control'}),
            'short_info': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'text': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'publish_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Author'})
        }