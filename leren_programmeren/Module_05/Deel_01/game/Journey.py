from game_storyline import storyline
from game_plaatjes import plaatjes
from game_over import game_over



soldaten = 20
geld = 100
naam = input("""---------- Welcome to Journey! ----------
Before we start, what is your name? """)
INTRO = input(f"""Hello {naam}! Here are some tips: You have 20 soldiers with you, and you start off with 100 coins. 
One of the first paths is harder than the other.
That is all you need to know for now. 
Good luck on your journey! Are you ready? (just type 'yes or no') """)
if INTRO == 'no':
    print("Then why are you playing this?")
elif INTRO == 'yes':
    while True:
        print(plaatjes[0])
        BEGIN = input(storyline[0]) 
        if BEGIN == 'forest':
            print(plaatjes[1])
            PAD1 = input(storyline[1])
            if PAD1 == 'elf village':
                ELF_DORP = input(storyline[2])
                if ELF_DORP == 'buy':
                    PRODUCTEN = input(storyline[3])
                    if PRODUCTEN == 'sword' or PRODUCTEN == 'pickaxe':
                        PAD2 = input(f"""You bought the {PRODUCTEN} for 30 coins from the shop, but you realize the rest of your team can't afford anything.
Eventually you reach the lake, but you need to get across.
How will you cross the river: swim or use a log (just type 'log')? """)
                        print(plaatjes[2])
                        if PAD2 == 'log':
                            print(plaatjes[3])
                            GROT = input(storyline[6])
                            if GROT == 'mine':
                               TROL = input(storyline[7])
                               if TROL == 'yell':
                                   MINEN = input(storyline[8])
                                   # Hier komt nog iets tussen.

        elif BEGIN == 'village':
            print(plaatjes[4])
            PAD1 = input(storyline[11])                 
            
else:
    BEGIN = input("Choose yes or no: ")