from django.db import models


class league(models.Model):
    id = models.IntegerField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    abbrName = models.CharField(max_length=50)

class nation(models.Model):
    id = models.IntegerField(primary_key=True, max_length=50)
    abbrName = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class club(models.Model):
    id = models.IntegerField(primary_key=True, max_length=50)
    abbrName = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    
class headshot(models.Model):
    pass
class traits(models.Model):
    pass
class specialities(models.Model):
    pass
class attributes(models.Model):
    pass

class Player(models.Model):
    commonName = models.CharField(max_length=50) # Example value Cristiano Ronaldo
    firstName = models.CharField(max_length=50) # Example value C. Ronaldo 
    lastName = models.CharField(max_length=50) # Example value dos Santos Aveiro 
    league_id = models.ForeignKey(league, on_delete=models.CASCADE) # Example value {} 
    nation_id = models.ForeignKey(nation, on_delete=models.CASCADE) # Example value {} 
    club_id = models.ForeignKey(club, on_delete=models.CASCADE) # Example value {} 
    headshot_id = models.ForeignKey(headshot, on_delete=models.CASCADE) # Example value {} 
    position = models.CharField(max_length=50) # Example value ST 
    composure = models.IntegerField() # Example value 99 
    playStyle = models.CharField(max_length=50) # Example value Basic 
    playStyleId = models.CharField(max_length=50, null=True) # Example value None 
    height = models.IntegerField() # Example value 187 
    weight = models.IntegerField() # Example value 83 
    birthdate = models.CharField(max_length=50) # Example value 02/05/1985 
    age = models.IntegerField() # Example value 36 
    acceleration = models.IntegerField() # Example value 95 
    aggression = models.IntegerField() # Example value 75 
    agility = models.IntegerField() # Example value 94 
    balance = models.IntegerField() # Example value 76 
    ballcontrol = models.IntegerField() # Example value 99 
    foot = models.CharField(max_length=50) # Example value Right 
    skillMoves = models.IntegerField() # Example value 5 
    crossing = models.IntegerField() # Example value 98 
    curve = models.IntegerField() # Example value 95 
    dribbling = models.IntegerField() # Example value 95 
    finishing = models.IntegerField() # Example value 99 
    freekickaccuracy = models.IntegerField() # Example value 89 
    gkdiving = models.IntegerField() # Example value 7 
    gkhandling = models.IntegerField() # Example value 11 
    gkkicking = models.IntegerField() # Example value 15 
    gkpositioning = models.IntegerField() # Example value 14 
    gkreflexes = models.IntegerField() # Example value 11 
    headingaccuracy = models.IntegerField() # Example value 99 
    interceptions = models.IntegerField() # Example value 41 
    jumping = models.IntegerField() # Example value 99 
    longpassing = models.IntegerField() # Example value 90 
    longshots = models.IntegerField() # Example value 99 
    marking = models.IntegerField() # Example value 40 
    penalties = models.IntegerField() # Example value 90 
    positioning = models.IntegerField() # Example value 99 
    potential = models.IntegerField() # Example value 94 
    reactions = models.IntegerField() # Example value 99 
    shortpassing = models.IntegerField() # Example value 95 
    shotpower = models.IntegerField() # Example value 99 
    slidingtackle = models.IntegerField() # Example value 32 
    sprintspeed = models.IntegerField() # Example value 98 
    standingtackle = models.IntegerField() # Example value 44 
    stamina = models.IntegerField() # Example value 99 
    strength = models.IntegerField() # Example value 95 
    vision = models.IntegerField() # Example value 96 
    volleys = models.IntegerField() # Example value 92 
    weakFoot = models.IntegerField() # Example value 4 
    traits_id = models.ForeignKey(traits, on_delete=models.CASCADE) # Example value [] 
    specialities_id = models.ForeignKey(specialities, on_delete=models.CASCADE) # Example value [] 
    atkWorkRate = models.CharField(max_length=50) # Example value High 
    defWorkRate = models.CharField(max_length=50) # Example value Low 
    playerType = models.CharField(max_length=50, null=True) # Example value None 
    attributes_id = models.ForeignKey(attributes, on_delete=models.CASCADE) # Example value [] 
    name = models.CharField(max_length=50) # Example value Cristiano Ronaldo 
    rarityId = models.IntegerField() # Example value 5 
    isIcon = models.CharField(max_length=50, null=True) # Example value False 
    quality = models.CharField(max_length=50) # Example value gold 
    isGK = models.CharField(max_length=50, null=True) # Example value False 
    positionFull = models.CharField(max_length=50) # Example value Striker 
    isSpecialType = models.CharField(max_length=50, null=True) # Example value False 
    contracts = models.CharField(max_length=50, null=True) # Example value None 
    fitness = models.CharField(max_length=50, null=True) # Example value None 
    rawAttributeChemistryBonus = models.CharField(max_length=50, null=True) # Example value None 
    isLoan = models.CharField(max_length=50, null=True) # Example value None 
    squadPosition = models.CharField(max_length=50, null=True) # Example value None 
    iconAttributes = models.CharField(max_length=50, null=True) # Example value None 
    itemType = models.CharField(max_length=50) # Example value player 
    discardValue = models.CharField(max_length=50, null=True) # Example value None 
    id = models.CharField(max_length=50) # Example value 100684097 
    modelName = models.CharField(max_length=50) # Example value FUTPlayerItem 
    baseId = models.IntegerField() # Example value 20801 
    rating = models.IntegerField() # Example value 99 
    



  
    

    
# "firstName": "C. Ronaldo",
# "lastName": "dos Santos Aveiro",
# "league": {},
# "nation": {},
# "club": {},
# "headshot": {},
# "position": "ST",
# "composure": 99,
# "playStyle": "Basic",
# "playStyleId": null,
# "height": 187,
# "weight": 83,
# "birthdate": "02/05/1985",
# "age": 36,
# "acceleration": 95,
# "aggression": 75,
# "agility": 94,
# "balance": 76,
# "ballcontrol": 99,
# "foot": "Right",
# "skillMoves": 5,
# "crossing": 98,
# "curve": 95,
# "dribbling": 95,
# "finishing": 99,
# "freekickaccuracy": 89,
# "gkdiving": 7,
# "gkhandling": 11,
# "gkkicking": 15,
# "gkpositioning": 14,
# "gkreflexes": 11,
# "headingaccuracy": 99,
# "interceptions": 41,
# "jumping": 99,
# "longpassing": 90,
# "longshots": 99,
# "marking": 40,
# "penalties": 90,
# "positioning": 99,
# "potential": 94,
# "reactions": 99,
# "shortpassing": 95,
# "shotpower": 99,
# "slidingtackle": 32,
# "sprintspeed": 98,
# "standingtackle": 44,
# "stamina": 99,
# "strength": 95,
# "vision": 96,
# "volleys": 92,
# "weakFoot": 4,
# "traits": [],
# "specialities": [],
# "atkWorkRate": "High",
# "defWorkRate": "Low",
# "playerType": null,
# "attributes": [],
# "name": "Cristiano Ronaldo",
# "rarityId": 5,
# "isIcon": false,
# "quality": "gold",
# "isGK": false,
# "positionFull": "Striker",
# "isSpecialType": false,
# "contracts": null,
# "fitness": null,
# "rawAttributeChemistryBonus": null,
# "isLoan": null,
# "squadPosition": null,
# "iconAttributes": null,
# "itemType": "player",
# "discardValue": null,
# "id": "100684097",
# "modelName": "FUTPlayerItem",
# "baseId": 20801,
# "rating": 99





# Create your models here.
