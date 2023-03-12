from django.urls import reverse
from django.utils import timezone
from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("main_app:home", kwargs={"slug": self.slug})
    
    def get_lastmod(self):
        return timezone.now()
    
