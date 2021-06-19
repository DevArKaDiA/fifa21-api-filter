from rest_framework import routers
from Api.views import PlayerViewSet



router = routers.DefaultRouter()
router.register(r'player', PlayerViewSet, basename="player")