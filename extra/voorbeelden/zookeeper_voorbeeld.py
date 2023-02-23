giraffen_aantal = 1
struisvogels_aantal = 1
zebras_aantal = 1

GIRAF_POTEN = 4
STRUISVOGEL_POTEN = 2
ZEBRA_POTEN = 4

def mijn_functie(giraffen, struisvogels, zebras):
    aantal_poten = giraffen_aantal * GIRAF_POTEN + struisvogels_aantal * STRUISVOGEL_POTEN + zebras_aantal * ZEBRA_POTEN
    return(aantal_poten)

print(mijn_functie())