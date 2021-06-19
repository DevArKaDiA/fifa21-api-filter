from typing import Dict, List
from django.core.management.base import BaseCommand, CommandError, CommandParser
from Api.models import Player, Team
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
                oldPlayer: Player = Player.objects.all().filter(fifa_id=player["id"]).first()

                team: Team = Team.objects.all().filter(teamName=player["club"]["name"]).first()

                if not team:
                    team = Team(teamName=player["club"]["name"])
                    team.save()


                print(player['commonName'])
                if oldPlayer:                    
                    oldPlayer.commonName=player['commonName'],
                    oldPlayer.firstName=player['firstName'],
                    oldPlayer.lastName=player['lastName'],
                    oldPlayer.position=player['position'],
                    oldPlayer.fifa_id=player['id']
                    oldPlayer.team=team
                    oldPlayer.save()
                else:
                    newPlayer = Player(
                        commonName=player['commonName'],
                        firstName=player['firstName'],
                        lastName=player['lastName'],
                        position=player['position'],                      
                        fifa_id=player['id'],
                        team=team,
                    )
                    newPlayer.save()


        initialRequest : dict = request()
        totalPages: int = initialRequest['totalPages']
        totalResults: int = initialRequest['totalResults']
        StorePlayers(initialRequest['items'])
        workers = []
        for page in range(initialRequest['page'] + 1, totalPages + 1):
            def requestAndSave(page):
                response = request(page)
                StorePlayers(response['items'])               

            
            workers.append(Thread(target=requestAndSave, args=[page]))
            if(len(workers) == 50):
                for worker in workers:
                    worker.start()
                for worker in workers:
                    worker.join()
                workers = []
            
            


        
        



        