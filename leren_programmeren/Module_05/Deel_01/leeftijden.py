# naam_lijst = []
# leeftijd_lijst= []

namen_en_leeftijden = {}

def mijn_functie():
        naam = input("Typ een naam in: ")
        namen_en_leeftijden['naam'] = naam
        leeftijd = int(input("Typ een leeftijd in: "))
        namen_en_leeftijden['leeftijd'] = leeftijd
        
        return namen_en_leeftijden
        # verder = input("Toets enter om door te gaan of 'stop' om te printen: ")
        # if verder == 'stop':
        #     break

    # return naam_lijst + leeftijd_lijst

print(mijn_functie())