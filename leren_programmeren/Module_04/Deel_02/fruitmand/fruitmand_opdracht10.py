from fruitmand import fruitmand
from operator import itemgetter

gewichten = sorted(fruitmand, key=itemgetter('weight'), reverse=True)

for fruit in gewichten:
    print(f"fruit: {fruit['name']}")
    print(f"gewicht: {fruit['weight']}")
    print("")