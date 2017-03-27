from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Year(models.Model):
    year = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.year

    def __str__(self):
        return self.year


class Player(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Score(models.Model):
    score = models.CharField(max_length=255)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.score

    def __str__(self):
        return self.score

