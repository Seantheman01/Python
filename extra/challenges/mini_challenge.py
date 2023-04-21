import random

lijstje = ["steen", "papier", "schaar"]
willekeurig = random.choice(lijstje)
print(willekeurig)
keuze = input("Kies steen, papier of schaar: ")

if keuze == willekeurig:
    print("Gelijkspel!")    