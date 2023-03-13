from game_storyline import storyline

soldaten = 20
geld = 100
while True:
    naam = input("""---------- Welcome to Journey! ----------
Before we start, what is your name? """)
    intro = input(f""" Hello {naam}! Here are some tips: You have 20 soldiers with you, and you start off with 100 coins. 
One of the first paths is harder than the other.
That is all you need to know for now. 
Good luck on your journey! Are you ready? (just type 'yes or no') """)
    if intro == 'no':
        print("Then why are you playing this?")
    elif intro == 'yes':
        begin = input(storyline[0])
    else:
        begin = input("Choose forest or village: ")