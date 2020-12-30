from django.conf import settings
from django.db import models

# Create your models here.
class headline(models.Model):
    title = models.CharField(max_length = 200)
    image = models.URLField(null = True, blank = True)
    url = models.TextField()

    def __str__(self):          #Print object data in human readable form
        return self.title
 