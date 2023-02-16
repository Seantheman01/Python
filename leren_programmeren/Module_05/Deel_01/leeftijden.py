mijn_lijst = []

def mijn_functie(x: int):
    naam = input("Typ een naam in: ")
    verder = input("Wil je doorgaan? Typ 'stop' als je wilt stoppen: ")
    mijn_lijst.append(naam)
    leeftijd = int(input("Typ een leeftijd in: "))
    mijn_lijst.append(leeftijd)
    print(naam + "is" + leeftijd + "jaar")

print(mijn_functie(mijn_functie))