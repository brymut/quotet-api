from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    # add image when s3 is set up
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    contact_type = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.contact_type

class HomepageInfo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.choice_text
    
    class Meta:
        verbose_name_plural = "Homepage Information"


class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    content = models.TextField()

    def __str__(self):
        return self.title