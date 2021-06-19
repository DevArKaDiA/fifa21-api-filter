from django.db import models
from django.db.models.deletion import CASCADE

# Los jugadores están en el response en el campo ítems,
# de estos interesa almacenar el nombre del jugador, 
# la posición en que juega, su nacionalidad y el nombre del
# equipo al que pertenece. 
# Adicionalmente debe iterar en hasta el numero de pagina que retorne el response del endpoint y guardar los jugadores en la base de datos.


class Team(models.Model):
    teamName = models.CharField(max_length=50)

class Player(models.Model):
    commonName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)     
    position = models.CharField(max_length=10)
    fifa_id = models.CharField(max_length=10)
    team = models.ForeignKey(Team, on_delete=CASCADE)

