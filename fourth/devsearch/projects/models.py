from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    featured_image = models.ImageField(default='default.jpg', upload_to='projects/%Y/%m/%d/')
    demo_link = models.CharField(max_length=2000, blank=True)
    source_link = models.CharField(max_length=2000, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
