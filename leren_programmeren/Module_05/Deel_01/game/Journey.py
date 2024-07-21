from game_storyline import storyline
from game_plaatjes import plaatjes
from game_over import game_over

invertory = {
    "Bag of money": {
        "amount": 200
    },
   
    "Steel sword": {
        "cost": 20,
        "damage": 15 
    }
}

wapens = {
    "Crystal sword": {
        
    }
}

print(plaatjes[0])
print(storyline[0])
pad_1 = input(storyline[1])

if pad_1 == "village" or "Village" or "VILLAGE":
    naar_binnen = input(storyline[2])
    if naar_binnen == "yes":
        pass