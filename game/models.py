from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime 
from django.utils import timezone

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
    pic1 = models.ImageField(upload_to='media/', blank=True, null=True)
    pic2 = models.ImageField(upload_to='media/', blank=True, null=True)
    pic3 = models.ImageField(upload_to='media/', blank=True, null=True)
    metacritic = models.IntegerField(default=0)
    text = models.TextField(default=" ")

    def __str__(self):
        return self.name

class Friends(models.Model):
    user = models.ForeignKey(User, default=None, related_name='user', on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)

    class Meta:
        verbose_name = 'Friend'

    def __str__(self):
        return self.user.username

class UserRequests(models.Model):
    user = models.ForeignKey(User, default=None, related_name='user_request', on_delete=models.CASCADE)
    requests = models.ManyToManyField(User, related_name='requests', blank=True)

    class Meta:
        verbose_name = 'User Request'

    def __str__(self):
        return self.user.username

class UserGamesInformation(models.Model):
    user = models.OneToOneField(User, default=None, primary_key=True, on_delete=models.CASCADE)
    currently_playing = models.ManyToManyField(Game, related_name='currently_playing', blank=True)
    want_to_play = models.ManyToManyField(Game, related_name='want_to_play', blank=True)
    finished = models.ManyToManyField(Game, related_name='finished', blank=True)

    class Meta:
        verbose_name = 'User Game Information'

    def __str__(self):
        return self.user.username
    
class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length='400')
    note = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{:s}, {:s}".format(self.author.username, self.game.name)