from game_storyline import storyline
from game_plaatjes import plaatjes
from game_over import game_over

jouw_aanvallen = """What will you do?:
Attack
Defend
Heal
"""

speler = {
    'health' : 100,
    'attack' : 'mace hit',
    'damage' : 25,
    'defense' : 1,
    'potions' : 1,
    'money' : 100
}

vijanden = {
    '1' : {
    'name' : 'goblin',
    'health' : 50,
    'attack' : 'dagger stab',
    'damage' : 20
    },
    '2' : {
    'name' : 'bounty hunter',
    'health' : 75,
    'attack' : 'sword slash',
    'damage' : 25
    }
}

def gevecht():
    while True:
        input(jouw_aanvallen)
        if jouw_aanvallen == "attack" or "Attack" or "ATTACK":
            print("You used " + speler['attack'] + " on the " + vijanden['1']['name'])
            vijanden['1']['health']-=speler['damage']
        
        if vijanden['1']['health'] == 0:
            print("You killed the " + vijanden['1']['name'] + " !")
            break

        else: 
            print("The " + vijanden['1']['name'] + " used " + vijanden['1']['attack'])
            speler['health']-=vijanden['1']['damage']

        if speler['health'] == 0:
            print(game_over[1])
            print("You died...")
            exit()

naam = input("""---------- Welcome to Journey! ----------
Before we start, what is your name? """)
intro = input(f"""
Hello {naam}! Here are some tips: you start off with 100 coins and 1 healing potion.
One of the first paths is harder than the other.
That is all you need to know for now. 
Good luck on your journey! Are you ready? (just type 'yes or no') """)
if intro == 'yes':
    begin = input(storyline[0]) 
    if begin == 'forest':
        print(plaatjes[1])
        print(storyline[1])
        print("A " + vijanden['1']['name'] + " appears!")
        print(plaatjes[8])
        gevecht()

        elf_dorp = input(storyline[2])
        speler.update({'health':100})
        if elf_dorp == 'sword' or "Sword" or "SWORD":
            speler['money']-=40
            speler['damage']+=10
            speler.update({'attack':'sword slash'})
            print(plaatjes[2])
            print("You bought the sword from the shop. Your damage increased!")
        elif elf_dorp == 'shield' or elf_dorp == "Shield" or elf_dorp=="SHIELD":
            speler['money']-=30
            speler['defense']+=1
            print(plaatjes[3])
            print("You bought the shield from the shop. Your defense increased!")

elif intro == 'no':
    print("Then why are you playing this?")