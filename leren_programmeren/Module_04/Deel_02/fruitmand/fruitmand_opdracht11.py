from fruitmand import fruitmand

kleuren = []
rond = 0
niet_rond = 0

for fruit in fruitmand:
    kleuren.append(fruit['color'])
    
while True:
    kleur_kiezen = input("Welke kleur wil je? Kies uit yellow, green, orange, red, brown: ")
    if kleur_kiezen not in kleuren:
        print(f"De kleur {kleur_kiezen} zit er niet in de fruitmand")
    else:
        break

for x in fruitmand:
    if x['color'] == kleur_kiezen:
        if x['round'] == True:
            rond += 1  
        else:
            niet_rond += 1

if rond > niet_rond:
    print(f"Er zijn {rond - niet_rond} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur_kiezen}")
elif rond < niet_rond:
    print(f"Er zijn {niet_rond - rond} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur_kiezen}")  
else:
    print(f"Er zijn {rond} ronde vruchten en {niet_rond} niet ronde vruchten in de kleur {kleur_kiezen}")