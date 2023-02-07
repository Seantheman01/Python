from fruitmand import fruitmand

langste_fruit = ''

for fruit in fruitmand:
    lengte = len(fruit['name'])
        
    if lengte > len(langste_fruit):
        langste_fruit = fruit['name']
        kleur = fruit['color']
        gewicht = fruit['weight']
        
print(f"De '{langste_fruit}' ({len(langste_fruit)} letters) heeft een {kleur} kleur en een gewicht van {gewicht} kg.")