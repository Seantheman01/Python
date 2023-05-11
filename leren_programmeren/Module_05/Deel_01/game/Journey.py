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
                    SPULLEN = input(storyline[3])
                    if SPULLEN == 'sword' or SPULLEN == 'pickaxe':
                        PAD2 = input(f"""You bought the {SPULLEN} for 30 coins from the shop, but you realize the rest of your team can't afford anything.
Eventually you reach the lake, but you need to get across.
How will you cross the river: swim or use a log (just type 'log')? """)
                        print(plaatjes[2])
                        if PAD2 == 'log':
                            print(plaatjes[3])
                            GROT = input(storyline[6])
                            if GROT == 'blocked':
                                print(game_over[3])
                                print(game_over[0])
                            elif GROT == 'mine':
                                TROL = input(storyline[7])
                                if TROL == 'fight':
                                    print(game_over[4])
                                    print(game_over[0])
                                elif TROL == 'yell':
                                   MINEN = input(storyline[8])
                                elif TROL == 'run':
                                    MINEN = input(storyline[9])
                                   # Hier komt nog iets tussen.
                                   
                elif ELF_DORP == 'steal':
                    SPULLEN = input(storyline[4])
                    if SPULLEN == 'continue':
                        PAD2 = input(storyline[5])
 
            elif PAD1 == 'swamp':
                print(game_over[2])
        elif BEGIN == 'village':
            print(plaatjes[4])
            PAD1 = input(storyline[11])
            if PAD1 == 'cheaper':
                MUUR = input(storyline[14])
                if MUUR == 'ask':
                    VERDER = input(storyline[15])
                    if VERDER == 'tell':
                        BANDIETEN = input(storyline[16])
                        if BANDIETEN == 'surrender':
                            print(game_over[5])
                            print(game_over[1])
                        elif BANDIETEN == 'fight':
                            BEWAKERS = input(storyline[18])
                        elif BANDIETEN == 'run':
                            BEWAKERS = input(storyline[17])
                            # Hier komt nog iets tussen.
                            
        OPNIEUW = input("Do you want to play again? ")
        if OPNIEUW == 'no':
            break
else:
    BEGIN = input("Choose yes or no: ")