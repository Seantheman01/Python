namen_en_leeftijden_lijst = []

def mijn_functie():
        namen_en_leeftijden_dict = {}
        naam = input("Typ een naam in: ")
        namen_en_leeftijden_dict['naam'] = naam
        leeftijd = int(input("Typ een leeftijd in: "))
        namen_en_leeftijden_dict['leeftijd'] = leeftijd

        return namen_en_leeftijden_dict

while True:
        namen_en_leeftijden_lijst.append(mijn_functie())
        verder = input("Toets enter om door te gaan of 'stop' om te printen: ")
        if verder == 'stop':
            break

for x in namen_en_leeftijden_lijst:
    print(f"{x['naam']} is {x['leeftijd']} jaar")