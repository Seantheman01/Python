naam_lijst = []
leeftijd_lijst= []

def mijn_functie(x: int):
    naam = input("Typ een naam in: ")
    naam_lijst.append(naam)
    verder = input("Toets enter om door te gaan of 'stop' om te printen: ")
    
    if verder != 'stop':
        leeftijd = int(input("Typ een leeftijd in: "))
        leeftijd_lijst.append(leeftijd)

print(mijn_functie(mijn_functie))