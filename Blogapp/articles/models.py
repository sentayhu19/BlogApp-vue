from django.db import models
from django.db.models.fields import SlugField

from django.conf import settings

# Create your models here.

class Article(models.Model):
    created_at = models.DateTimeField(auto_created= True)
    title = models.CharField(max_length= 300)
    body = models.TextField()
    slug = SlugField(max_length= 250, unique= True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete= models.CASCADE,
                            related_name= "articles" )
    def __str__(self):
        return self.title