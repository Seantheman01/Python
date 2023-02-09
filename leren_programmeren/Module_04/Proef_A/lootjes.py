import random

namen = []
lootjes = []
teller = 0
random_naam = 0
random_lootje = 0

while True:
    naam_invullen = input("Vul een naam in: ")
    if naam_invullen not in namen:
        namen.append(naam_invullen)
        lootjes.append(naam_invullen)
        teller += 1
    else:
        print("Die naam is er al!")
        
    naam_toevoegen = input("Wil je nog een naam toevoegen? Typ ja of nee: ")
    if naam_toevoegen == 'nee' and teller <=2:
        print("Je moet meer namen toevoegen!")
    elif naam_toevoegen == 'nee' and teller >=3:
        break

while True:
    if namen[random_naam] == lootjes[random_naam]:
        random.shuffle(lootjes)
        random_naam = 0
    else:
        random_naam += 1

    if random_naam >= 3:
        break

for x in namen:
    print(f'{namen[random_lootje]} heeft {lootjes[random_lootje]}')
    random_lootje += 1