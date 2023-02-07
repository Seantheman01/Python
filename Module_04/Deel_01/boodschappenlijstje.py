lijstje = {}

while True:
    boodschap = input("Welke boodschappen heb je nodig? ")
    hoeveelheid = int(input("Hoeveel heb je daarvan nodig? "))

    if boodschap not in lijstje:
        lijstje[boodschap] = hoeveelheid
    else:
        lijstje[boodschap] += hoeveelheid
    
    verder = input("Heb je meer spullen nodig? ")
    if verder == 'nee':
        break
    elif verder != 'ja' and verder != 'nee':
        input("Vul ja of nee in: ")
        
print("-[ BOODSCHAPPENLIJSTJE ]-")   
for x in lijstje:
    print(f"{lijstje[x]}x {x}")
print("-------------------------")