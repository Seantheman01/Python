namen_en_leeftijden_dict = {}
namen_en_leeftijden_lijst = []

def mijn_functie():
        naam = input("Typ een naam in: ")
        namen_en_leeftijden_dict['naam'] = naam
        leeftijd = int(input("Typ een leeftijd in: "))
        namen_en_leeftijden_dict['leeftijd'] = leeftijd
  
        return namen_en_leeftijden_dict

while True:
        mijn_functie()
        verder = input("Toets enter om door te gaan of 'stop' om te printen: ")
        if verder == 'stop':
            break
        else:
            namen_en_leeftijden_lijst.append(mijn_functie())
            
print()