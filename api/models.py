from django.db import models
from django.contrib.postgres.fields import ArrayField


class UserPokemon(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    pokemon = ArrayField(models.IntegerField())
