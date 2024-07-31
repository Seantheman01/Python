print("Welkom bij Papi Gelato. Je mag alle smaken kiezen zolang het maar vanille ijs is.")

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

aantal_bolletjes()