giraf_aantal = int(input("Hoeveel giraffen zijn er? "))
struisvogel_aantal = int(input("Hoeveel struisvogels zijn er? "))
zebra_aantal = int(input("Hoeveel zebra's zijn er? "))

# giraf_aantal = 1
# struisvogel_aantal = 1
# zebra_aantal = 1

GIRAF_POTEN = 4
STRUISVOGEL_POTEN = 2
ZEBRA_POTEN = 4

def mijn_functie(giraffen, struisvogels, zebras):
    aantal_poten = giraf_aantal * GIRAF_POTEN + struisvogel_aantal * STRUISVOGEL_POTEN + zebra_aantal * ZEBRA_POTEN
    return aantal_poten

print(mijn_functie())
# print(mijn_functie(5,3,2)) dit kan
# print(mijn_functie(5,3,zebra_aantal)) dit kan ook
# print(giraf_aantal, struisvogel_aantal, zebra_aantal)) en dit ook