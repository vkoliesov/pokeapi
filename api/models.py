from django.db import models


class UserPokemon(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    pokemon_id = models.IntegerField()

    def __str__(self):
        return f'({self.user},{self.pokemon})' 
