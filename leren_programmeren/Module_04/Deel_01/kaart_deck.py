import random

vormen = ('harten', 'klaveren', 'schoppen', 'ruiten')
soorten = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw','heer', 'aas')
jokers = ('joker1', 'joker2')
kaarten = []
aantal = 1

for x in range(len(jokers)):
    kaarten.append(jokers[x])

for vorm in vormen:
    for soort in soorten:
        kaarten.append(vorm + " " + soort)

random.shuffle(kaarten)

for y in range(7):
    print(f"kaart {aantal}: {kaarten[0]}")
    kaarten.pop(0)
    aantal += 1
    
print(f"deck {len(kaarten)} kaarten: {kaarten}")