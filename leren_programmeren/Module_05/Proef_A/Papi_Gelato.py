print("Welkom bij Papi Gelato. Je mag alle smaken kiezen zolang het maar vanille ijs is.")

aantal = int(input("Hoeveel bolletjes wilt u? "))
if aantal == 1 or aantal == 2 or aantal == 3:
    soort = input(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje?")
    if soort == "hoorntje" or soort == "bakje":
        print(f"Hier is uw {soort} met {aantal} bolletje(s).")