from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name =  models.CharField(max_length=250)
    host =  models.CharField(max_length=100)
    credit =  models.CharField(max_length=250)
    hostId =  models.CharField(max_length=100)

class RecipeLike(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)