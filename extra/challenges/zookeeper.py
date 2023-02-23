# opdracht 1:
def mijn_functie():
    giraf_aantal = int(input("Hoeveel giraffen zijn er? "))
    struisvogel_aantal = int(input("Hoeveel struisvogels zijn er? "))
    zebra_aantal = int(input("Hoeveel zebra's zijn er? "))

    GIRAF_POTEN = 4
    STRUISVOGEL_POTEN = 2
    ZEBRA_POTEN = 4
    
    aantal_poten = giraf_aantal * GIRAF_POTEN + struisvogel_aantal * STRUISVOGEL_POTEN + zebra_aantal * ZEBRA_POTEN
    return(aantal_poten)

print(f"Er zijn {mijn_functie()} poten.")