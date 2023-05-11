from game_storyline import storyline
from game_plaatjes import plaatjes
from game_over import game_over

def geld_eraf(n1, n2):
    return n1 - n2

def soldaten_eraf(n3, n4):
    return n3 - n4

soldaten = 20
geld = 100
naam = input("""---------- Welcome to Journey! ----------
Before we start, what is your name? """)
intro = input(f"""Hello {naam}! Here are some tips: You have 20 soldiers with you, and you start off with 100 coins. 
One of the first paths is harder than the other.
That is all you need to know for now. 
Good luck on your journey! Are you ready? (just type 'yes or no') """)
if intro == 'no':
    print("Then why are you playing this?")
elif intro == 'yes':
    while True:
        print(plaatjes[0])
        begin = input(storyline[0]) 
        if begin == 'forest':
            print(plaatjes[1])
            pad1 = input(storyline[1])
            if pad1 == 'elf village':
                elf_dorp = input(storyline[2])
                if elf_dorp == 'buy':
                    spullen = input(storyline[3])
                    if spullen == 'sword' or spullen == 'pickaxe':
                        print(f"""You bought the {spullen} from the shop, but you realize the rest of your team can't afford anything.""")
                        geld_over = geld_eraf(geld, 50)

                elif elf_dorp == 'steal':
                    soldaten_over = soldaten_eraf(soldaten, 5)
                    spullen = input(storyline[4])
                    if spullen == 'continue':
                        print(storyline[5])  

                    print(plaatjes[2])
                    pad2 = ("""Eventually you reach the lake, but you need to get across.
How will you cross the river: swim or use a log (just type 'log')? """)  
                    if pad2 == 'log':
                        print(plaatjes[3])
                        grot = input(storyline[6])
                        if grot == 'blocked':
                            print(game_over[3])
                            print(game_over[0])
                        elif grot == 'mine':
                            trol = input(storyline[7])
                            if trol == 'fight':
                                print(game_over[4])
                                print(game_over[0])
                            elif trol == 'yell':
                                minen = input(storyline[8])
                            elif trol == 'run':
                                minen = input(storyline[9])
                                soldaten_over = soldaten_eraf(soldaten, 6)

                            if elf_dorp == 'pickaxe' and minen == 'yes':
                                pad3 = input(storyline[19])
                            elif elf_dorp == 'pickaxe' and minen == 'no':
                                pad3 = input(storyline[20])
                            elif elf_dorp == 'sword' and minen == 'yes':
                                pad3 = input(storyline[21])
                            elif elf_dorp == 'sword' and minen == 'no':
                                pad3 = input(storyline[20])
                            elif elf_dorp == 'continue' and minen == 'yes':
                                pad3 = input(storyline[19])
                            elif elf_dorp == 'continue' and minen == 'no':
                                pad3 = input(storyline[20])
                                # Hier komt nog iets tussen.

            elif pad1 == 'swamp':
                print(game_over[2])
                print(game_over[0])

        elif begin == 'village':
            print(plaatjes[4])
            pad1 = input(storyline[11])
            if pad1 == 'cheaper':
                muur = input(storyline[14])
            elif pad1 == 'steal':
                muur = input(storyline[12])
                soldaten_over = soldaten_eraf(soldaten, 5)

            if muur == 'threaten':
                print(game_over[5])
                print(game_over[1])
            elif muur == 'ask':
                verder = input(storyline[15])
                if verder == 'tell':
                    bandieten = input(storyline[16])
                    if bandieten == 'surrender':
                        print(game_over[6])
                        print(game_over[1])
                    elif bandieten == 'fight':
                        bewakers = input(storyline[18])
                    elif bandieten == 'run':
                        bewakers = input(storyline[17])
                        # Hier komt nog iets tussen.

        opnieuw = input("Do you want to play again? ")
        if opnieuw == 'no':
            break
        print(geld_over)
        print(soldaten_over)
else:
    begin = input("Choose yes or no: ")