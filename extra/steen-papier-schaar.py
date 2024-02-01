import random

while True:
    lijstje = ["steen", "papier", "schaar"]
    willekeurig = random.choice(lijstje)
    keuze = input("Kies steen, papier of schaar: ")

    if keuze == willekeurig:
        print(willekeurig)
        print("Gelijkspel!")
    elif willekeurig == "steen" and keuze == "papier":
        print(willekeurig)
        print("Je hebt gewonnen!")
    elif willekeurig == "steen" and keuze == "schaar":
        print(willekeurig)
        print("Je hebt verloren!")
    elif willekeurig == "papier" and keuze == "schaar":
        print(willekeurig)
        print("Je hebt gewonnen!")
    elif willekeurig == "papier" and keuze == "steen":
        print(willekeurig)
        print("Je hebt verloren!")
    elif willekeurig == "schaar" and keuze == "steen":
        print(willekeurig)
        print("Je hebt gewonnen!")
    elif willekeurig == "schaar" and keuze == "papier":
        print(willekeurig)
        print("Je hebt verloren!")
    elif keuze == "stop":
        break