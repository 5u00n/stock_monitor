from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Stock(models.Model):
    watchlist = models.ForeignKey(Watchlist, related_name='stocks', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
