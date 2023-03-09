from fruitmand import fruitmand
kleuren = []

for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)
    
for x in fruitmand:
    if x['color'] not in kleuren:
        kleuren.append(x['color'])
print(kleuren)