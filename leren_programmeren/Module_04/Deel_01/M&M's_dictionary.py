import random

kleuren = ["rood", "blauw", "groen", "geel", "bruin"]
aantal = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden? "))
inhoud = {}

for x in range(aantal):
    random_kleur = random.choice(kleuren)
    
    if random_kleur not in inhoud:
        inhoud[random_kleur] = 1
    else:
        inhoud[random_kleur] += 1
    
print(inhoud)