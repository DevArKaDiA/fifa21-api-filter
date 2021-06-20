from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets, mixins

# from rest_framework import permissions
from Api.serializers import PlayerSerializer, TeamSerializer
from Api.models import Player, Team



class PlayerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows Players to be viewed or edited.
    """
    serializer_class = PlayerSerializer
    # queryset = Player.objects.all()#.order_by('-commonName')
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `player` query parameter in the URL.
        """
        queryset = Player.objects.all()
        
        name = self.request.query_params.get('name')
        order = self.request.query_params.get('order')        
        
        if name is not None:
            queryset = queryset.filter(commonName__icontains=name)

        if order is not None:
            queryset = queryset.order_by("commonName" if order == "asc" else "-commonName")
        else:
            queryset = queryset.order_by("commonName")            
            
        return queryset



@api_view(['POST'])
def TeamPlayersView(request):
    if request.method == 'POST':        
        if "Name" in request.data:
            selectedTeam: Team = Team.objects.all().filter(teamName__icontains=request.data['Name']).first()
            if selectedTeam:
                Players = TeamSerializer(selectedTeam).data
                
                return JsonResponse({
                    'TeamName': selectedTeam.teamName,
                    'Players' : Players['player_set']
                    })
            else:
                return JsonResponse({
                    'message': "Team don't found"
                })
    

