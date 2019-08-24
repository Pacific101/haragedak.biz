from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify


class Profile(models.Model):
    email_confirmed = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    image = models.ImageField(blank=True,upload_to='main_app/',default='main_app/default.png')

class Restraunt(models.Model):
    name = models.CharField(max_length=264,blank=True)
    address = models.CharField(max_length=264)
    address_link = models.CharField(max_length=400)
    website = models.URLField(max_length=264)
    opening_hour = models.TimeField(blank=True,null=True)
    closing_hour = models.TimeField(blank=True,null=True)
    type = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    area = models.CharField(max_length=264,null=False)
    image = models.ImageField(upload_to='main_app')
    map = models.CharField(max_length=600)
    description = models.CharField(max_length=15000)
    short_desc = models.CharField(max_length=60)
    average = models.IntegerField(blank=True,null=True,max_length=600)
    link1 = models.CharField(blank=True,null=True,max_length=600)
    link2 = models.CharField(blank=True,null=True,max_length=600)
    link3 = models.CharField(blank=True,null=True,max_length=600)
    link4 = models.CharField(blank=True,null=True,max_length=600)
    link5 = models.CharField(blank=True,null=True,max_length=600)

    def __str__(self):
        return self.name

class Bookmark(models.Model):
    name = models.CharField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='bookmarks')
    restaurant = models.ForeignKey(Restraunt,on_delete=models.CASCADE,related_name='bookmarkz',blank=True,null=True)

    def __str__(self):
        return self.name



class Beauty(models.Model):
    name = models.CharField(max_length=264,blank=True)
    address = models.CharField(max_length=264)
    address_link = models.CharField(max_length=400)
    website = models.URLField(max_length=264)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    phone = models.CharField(max_length=200)
    area = models.CharField(max_length=264,null=False)
    image = models.ImageField(upload_to='main_app')
    map = models.CharField(max_length=600)
    description = models.CharField(max_length=15000)
    short_desc = models.CharField(max_length=60)
    average = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class Hotels(models.Model):
    name = models.CharField(max_length=264,blank=True)
    address = models.CharField(max_length=264)
    address_link = models.CharField(max_length=400)
    website = models.URLField(max_length=264)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    phone = models.CharField(max_length=200)
    area = models.CharField(max_length=264,null=False)
    image = models.ImageField(upload_to='main_app')
    map = models.CharField(max_length=600)
    description = models.CharField(max_length=15000)
    short_desc = models.CharField(max_length=60)
    average = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class Shopping(models.Model):
    name = models.CharField(max_length=264,blank=True)
    address = models.CharField(max_length=264)
    address_link = models.CharField(max_length=400)
    website = models.URLField(max_length=264)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    phone = models.CharField(max_length=200)
    area = models.CharField(max_length=264,null=False)
    image = models.ImageField(upload_to='main_app')
    map = models.CharField(max_length=600)
    description = models.CharField(max_length=15000)
    short_desc = models.CharField(max_length=60)
    average = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class Coffee(models.Model):
    name = models.CharField(max_length=264,blank=True)
    address = models.CharField(max_length=264)
    address_link = models.CharField(max_length=400)
    website = models.URLField(max_length=264)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    phone = models.CharField(max_length=200)
    area = models.CharField(max_length=264,null=False)
    image = models.ImageField(upload_to='main_app')
    map = models.CharField(max_length=600)
    description = models.CharField(max_length=15000)
    short_desc = models.CharField(max_length=60)
    average = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class Bars(models.Model):
    name = models.CharField(max_length=264,blank=True)
    address = models.CharField(max_length=264)
    address_link = models.CharField(max_length=400)
    website = models.URLField(max_length=264)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    phone = models.CharField(max_length=200)
    area = models.CharField(max_length=264,null=False)
    image = models.ImageField(upload_to='main_app')
    map = models.CharField(max_length=600)
    description = models.CharField(max_length=15000)
    short_desc = models.CharField(max_length=60)
    average = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class Automotive(models.Model):
    name = models.CharField(max_length=264,blank=True)
    address = models.CharField(max_length=264)
    address_link = models.CharField(max_length=400)
    website = models.URLField(max_length=264)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()
    phone = models.CharField(max_length=200)
    area = models.CharField(max_length=264,null=False)
    image = models.ImageField(upload_to='main_app')
    map = models.CharField(max_length=600)
    description = models.CharField(max_length=15000)
    short_desc = models.CharField(max_length=60)
    average = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    restraunt = models.ForeignKey(Restraunt, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reviewed')
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    rating = models.FloatField(default=0,blank=False,null=False)

    def approve(self):
        self.approved_review = True
        self.save()

    def __str__(self):
        return self.title
