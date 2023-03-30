from game_storyline import storyline
from game_plaatjes import plaatjes
from game_GAME_OVER import GAME_OVER

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
else:
    BEGIN = ("Choose yes or no")