mijn_lijst = []

def mijn_functie(x: int):
    naam = input("Typ een naam in: ")
    mijn_lijst.append(naam)
    verder = input("Toets enter om door te gaan of 'stop' om te printen: ")
    
    if verder != 'stop':
        leeftijd = int(input("Typ een leeftijd in: "))
        mijn_lijst.append(leeftijd)
        
    # print(naam + "is" + leeftijd + "jaar")

print(mijn_functie(mijn_functie))