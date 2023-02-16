mijn_lijst = []

def mijn_functie(x: int):
    naam = input("Typ een naam in: ")
    mijn_lijst.append(naam)
    verder = input("Wil je doorgaan? Typ ja als je door wilt gaan, typ 'stop' als je wilt stoppen: ")
    leeftijd = int(input("Typ een leeftijd in: "))
    mijn_lijst.append(leeftijd)
    print(naam + "is" + leeftijd + "jaar")

print(mijn_functie(mijn_functie))