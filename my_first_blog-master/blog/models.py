from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): #определяет обьект
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #для перехода на другую модель
    title = models.CharField(max_length=200)#для лимитного письма
    text = models.TextField()# для безлимитного письма
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
