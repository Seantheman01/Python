print("Welkom bij Papi Gelato. Je mag alle smaken kiezen zolang het maar vanille ijs is.")

while True:
    def aantal_bolletjes():
        while True:
            aantal = int(input("Hoeveel bolletjes wilt u? "))
            if aantal >= 1 and aantal <= 3:
                break
            elif aantal >= 4 and aantal <= 8:
                print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes.')
                break
            elif aantal > 8:
                print('Sorry, zulke grote bakken hebben we niet.')
            else:
                print("Sorry dat snap ik niet...")

    aantal = aantal_bolletjes()


    def hoorn_of_bak():
        while True:
            soort = input(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ")
            if soort == "hoorntje" or soort == "bakje":
                break
            else:
                print("Sorry dat snap ik niet...")

    soort = hoorn_of_bak()


    def meer_bestellen():
        while True:
            print(f"Hier is uw {soort} met {aantal} bolletje(s).")
            opnieuw = input("Wilt u nog meer bestellen? ")
            if opnieuw == "ja":
                break
            elif opnieuw == "nee":
                print("Bedankt en tot ziens!")
                break
            else:
                print("Sorry dat snap ik niet...")

    opnieuw = meer_bestellen()