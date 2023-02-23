# opdracht 1:
def mijn_functie():
    giraffen_aantal = int(input("Hoeveel giraffen zijn er? "))
    struisvogels_aantal = int(input("Hoeveel struisvogels zijn er? "))
    zebras_aantal = int(input("Hoeveel zebra's zijn er? "))

    GIRAF_POTEN = 4
    STRUISVOGEL_POTEN = 2
    ZEBRA_POTEN = 4
    
    som = (giraffen_aantal * GIRAF_POTEN) + (struisvogels_aantal * STRUISVOGEL_POTEN) + (zebras_aantal * ZEBRA_POTEN)
    return(som)

print(f"Er zijn {mijn_functie()} poten.")