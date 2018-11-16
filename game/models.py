from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Developer(models.Model):
    name = models.CharField(max_length=40)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Mode(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=40)
    release_date = models.DateField()
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    platforms = models.ManyToManyField(Platform)
    modes = models.ManyToManyField(Mode)
    pic = models.ImageField(upload_to='media/')
    metacritic = models.IntegerField(default=0)
    text = models.TextField(default=" ")

    def __str__(self):
        return self.name



