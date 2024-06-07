from django.db import models


class Main(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='main/images/')
    url = models.URLField(blank=True)
