def mijn_functie():
    giraffen_aantal = int(input("Hoeveel giraffen zijn er? "))
    struisvogels_aantal = int(input("Hoeveel struisvogels zijn er? "))
    zebras_aantal = int(input("Hoeveel zebra's zijn er? "))

    giraf_poten = 4
    struisvogel_poten = 2
    zebra_poten = 4
    
    som = (giraffen_aantal * giraf_poten) + (struisvogels_aantal * struisvogel_poten) + (zebras_aantal * zebra_poten)
    return(som)

print(mijn_functie())