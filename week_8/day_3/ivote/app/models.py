from django.db import models

# Create your models here.
class Voter(models.Model):
    tz = models.IntegerField(unique=True)
    name = models.TextField(max_length=60)
    isVote = models.BooleanField(default=False)

class Party(models.Model):
    name = models.TextField(max_length=60)
    votes = models.IntegerField(default=0)