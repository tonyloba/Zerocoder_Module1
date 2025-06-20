from django.db import models
from django.contrib.auth.models import User

class News_Posts(models.Model):
    title = models.CharField('TitleNews', max_length=50)
    short_info = models.CharField('Short Description', max_length=200)
    text = models.TextField('TextNews')
    publish_date = models.DateTimeField('Date of publication')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Author')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'All News'