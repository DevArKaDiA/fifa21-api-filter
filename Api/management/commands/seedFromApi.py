from typing import Dict, List
from django.core.management.base import BaseCommand, CommandError, CommandParser
from Api.models import Player
from threading import Thread
import requests as rq
import json

class Command(BaseCommand):
    help = "Seed players from 3 party API"
    
    def handle(self, *args, **options) -> dict:
        def request(page: int = 1):
            response = rq.get('https://www.easports.com/fifa/ultimate-team/api/fut/item?page={}'.format(page))
            responseBody: dict = response.json()
            if response.status_code != 200:
                return None            
            return responseBody

        def StorePlayers(items: list = []) -> None:            
            for player in items:
                oldPlayer: Player = Player.objects.filter(fifa_id=player["id"])[0]
                if oldPlayer:                    
                    oldPlayer.commonName=player['commonName'],
                    oldPlayer.firstName=player['firstName'],
                    oldPlayer.lastName=player['lastName'],
                    oldPlayer.position=player['position'],
                    oldPlayer.fifa_id=player['id']
                    oldPlayer.save()
                else:
                    newPlayer = Player(
                        commonName=player['commonName'],
                        firstName=player['firstName'],
                        lastName=player['lastName'],
                        position=player['position'],
                        fifa_id=player['id'],
                    )
                    newPlayer.save()


        initialRequest : dict = request()
        totalPages: int = initialRequest['totalPages']
        totalResults: int = initialRequest['totalResults']
        StorePlayers(initialRequest['items'])
        for page in range(initialRequest['page'] + 1, totalPages + 1):
            def requestAndSave(page):
                response = request(page)
                StorePlayers(response['items'])
                print(page)
            pageWorker = Thread(target=requestAndSave, args=[page])
            pageWorker.start()                        
            
            


        
        



        