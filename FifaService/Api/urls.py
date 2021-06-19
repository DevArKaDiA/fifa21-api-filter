from django.urls.conf import include
from rest_framework import routers
from Api.views import PlayerViewSet, TeamPlayersView
from django.urls import path


router = routers.DefaultRouter()
router.register(r'player', PlayerViewSet, basename="player")


url = [
    path('team', TeamPlayersView),    
]
