nieuwe_lijst = []

def mijn_functie(x: int):
        nieuwe_dictionairy = {}
        naam = input("Typ een naam in: ")
        leeftijd = int(input("Typ een leeftijd in: "))
        verder = input("Toets enter om door te gaan of 'stop' om te printen: ")
        nieuwe_dictionairy['naam'] = naam
        nieuwe_dictionairy['leeftijd'] = leeftijd
        if verder != 'stop':
            return nieuwe_dictionairy

while True:
    