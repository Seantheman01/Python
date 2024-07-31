print("Welkom bij Papi Gelato. Je mag alle smaken kiezen zolang het maar vanille ijs is.")

def aantal_bolletjes():
    aantal = int(input("Hoeveel bolletjes wilt u? "))
    if aantal >= 1 and aantal <= 3:
        pass
    elif aantal >= 4 and aantal <= 8:
        print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes.')
    elif aantal > 8:
        print('Sorry, zulke grote bakken hebben we niet.')
    else:
        print("Sorry dat snap ik niet...")
            
# return aantal_bolletjes

aantal = aantal_bolletjes()


def hoorn_of_bak():
    soort = input(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ")
    if soort == "hoorntje" or soort == "bakje":
        pass
        
# return hoorn_of_bak

hoorn_of_bak()