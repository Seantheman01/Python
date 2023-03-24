from game_storyline import storyline
from game_plaatjes import plaatjes

soldaten = 20
geld = 100
naam = input("""---------- Welcome to Journey! ----------
Before we start, what is your name? """)
INTRO = input(f""" Hello {naam}! Here are some tips: You have 20 soldiers with you, and you start off with 100 coins. 
One of the first paths is harder than the other.
That is all you need to know for now. 
Good luck on your journey! Are you ready? (just type 'yes or no') """)

if INTRO == 'no':
    print("Then why are you playing this?")
elif INTRO == 'yes':
    print(plaatjes[0])
    BEGIN = input(storyline[0])
    if BEGIN == 'forest':
        print(plaatjes[1])
        PAD1 = input(storyline[1])
        if PAD1 == 'elf village':
            SPULLEN = input(storyline[2])
            if SPULLEN == 'buy':
                ELF_WINKEL = input(storyline[3])
                
else:
    BEGIN = ("Choose yes or no")