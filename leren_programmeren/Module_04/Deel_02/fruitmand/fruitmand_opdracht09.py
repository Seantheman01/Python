from fruitmand import fruitmand

for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove()
    
for x in fruitmand:
    print(x['color'])