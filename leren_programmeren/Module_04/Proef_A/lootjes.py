import random

namen = []
teller = 0

while True:
    naam_invullen = input("Vul een naam in: ")
    namen.append(naam_invullen)
    teller += 1
    naam_toevoegen = input("Wil je nog een naam toevoegen? Typ ja of nee: ")
    
    if naam_toevoegen == 'nee' and teller <=2:
        print("Je moet meer namen toevoegen!")
    elif naam_toevoegen == 'nee' and teller >=3:
        break

for x in namen:
    print(f"{random.choice(namen)} heeft {random.choice(namen)}")
    
if naam_invullen in namen:
        random.shuffle(namen)