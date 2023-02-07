from schoenen_data import schoenen_lijst


# opdracht 1:
# Print alle schoenen van het merk Adidas
for x in schoenen_lijst:
    if x['merk'] == 'Adidas':
        print(x)

# filteren
# opdracht 2:
# Vraag een merk en print vervolgens alle modellen van het merk en de bijbehorende prijs.
vraag_merk = input("Welk merk? Kies uit Adidas, Nike, Puma of Gaastra: ")
for x in schoenen_lijst:
    if vraag_merk != '':
        print(x['merk'])
        print(x['model'])
        print(x['prijs'])
    
    
# opdracht 3:
# Vraag een merk en print vervolgens alle witte schoenen mits duurder dan €100.


# opdracht 4:
# vraag de maat van de klant en print vervolgens:
# "fonetische_kleuren Merknaam Modelnaam, prijs"
# uiteraard alleen de schoenen die beschikbaar zijn in betreffende maat.


# Opdracht 5 (medium):
# print van de duurste schoen: merk en model en doe dat ook voor de goedkoopste.


# opdracht 6 (hard):
# print van de schoen leverbaar in de grootste maat :
# IN maat ... leverbaar: merk. model en kleur van de schoenen
# (let op, filter in: in code)