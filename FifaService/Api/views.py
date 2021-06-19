from django.views import generic
from rest_framework import viewsets, mixins
from rest_framework.response import Response
# from rest_framework import permissions
from Api.serializers import PlayerSerializer
from Api.models import Player



class PlayerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PlayerSerializer
    # queryset = Player.objects.all()#.order_by('-commonName')
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Player.objects.all()
        
        name = self.request.query_params.get('name')
        order = self.request.query_params.get('order')        
        
        if name is not None:
            queryset = queryset.filter(commonName__contains=name)

        if order is not None:
            queryset = queryset.order_by("commonName" if order == "asc" else "-commonName")
        else:
            queryset = queryset.order_by("commonName")
            
            
        return queryset

