from game_storyline import storyline
from game_plaatjes import plaatjes
from game_over import game_over

jouw_aanvallen = """What will you do?:
Attack
Defend
Heal
"""

# speler = {
#     'health' : 100,
#     'attack' : 'sword slash',
#     'damage' : 25,
#     'potions' : 1,
#     'money' : 100
# }

vijanden = {
    'creature' : 'goblin',
    'health' : 50,
    'attack' : 'knife stab',
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
        elf_winkel = input(storyline[1])
        if elf_winkel == 'sword':
            print(plaatjes[2])
            print("""You bought the sword from the shop. 
Your attack increased!""")
        elif elf_winkel == 'shield':
            print(plaatjes[3])
            print("""You bought the shield from the shop. 
Your defense increased!""")
        elif elf_winkel == 'none':
            print("You bought nothing from the shop.")

        print(storyline[2])

        print("Suddenly, a " + vijanden["creature"] + " appears")
        print(plaatjes[8])

        input(jouw_aanvallen)
        if jouw_aanvallen == "attack" or "Attack" or 'ATTACK':
            print("You attacked the " + vijanden['creature'])
            vijanden['health']-=25
            print(vijanden['health'])
        elif jouw_aanvallen == "defend" or "Defend" or "DEFEND":
            print("You defended yourself")
            print(vijanden['health'])

elif intro == 'no':
    print("Then why are you playing this?")