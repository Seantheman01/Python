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
    'attack' : 'sword slash',
    'damage' : 25,
    'defense' : 1,
    'potions' : 1,
    'money' : 100
}

vijanden = {
    'creature' : 'goblin',
    'health' : 50,
    'attack' : 'dagger stab',
    'damage' : 20
}

naam = input("""---------- Welcome to Journey! ----------
Before we start, what is your name? """)
intro = input(f"""
Hello {naam}! Here are some tips: you start off with 100 coins,
and one of the first paths is harder than the other.
That is all you need to know for now. 
Good luck on your journey! Are you ready? (just type 'yes or no') """)
if intro == 'yes':
    print(plaatjes[0])
    begin = input(storyline[0]) 
    if begin == 'forest':
        print(plaatjes[1])
        print(storyline[1])

        print("A " + vijanden["creature"] + " appears!")
        print(plaatjes[8])

        while True:
            input(jouw_aanvallen)
            if jouw_aanvallen == "attack" or "Attack" or 'ATTACK':
                print("You used " + speler['attack'] + " on the " + vijanden['creature'])
                vijanden['health']-=speler['damage']
            
            if vijanden['health'] == 0:
                print("You killed the goblin!")
                break

            else: 
                print("The goblin used " + vijanden['attack'])
                speler['health']-=vijanden['damage']
            if speler['health'] == 0:
                print(game_over[1])
                print("You died...")
                exit()

        elf_dorp = input(storyline[2])
        speler.update({'health': 100})
        if elf_dorp == 'sword':
            speler['money']-=40
            speler['damage']+=10
            print(plaatjes[2])
            print("You bought the sword from the shop. Your attack increased!")
        elif elf_dorp == 'shield':
            speler['money']-=30
            speler['defense']+=1
            print(plaatjes[3])
            print("You bought the shield from the shop. Your defense increased!")
        # elif elf_dorp == 'none':
        #     print("You bought nothing from the shop.")

elif intro == 'no':
    print("Then why are you playing this?")