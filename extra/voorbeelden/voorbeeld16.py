def bereken_btw_over_bedrag(bedrag: float, btw_percentage: int) -> float:
    bedrag_inc = (bedrag * (100 + btw_percentage)) / 100
    return round(bedrag_inc, 2)

regels_excl = [63.15, 52.25]
regels_incl = []

for el in regels_excl:
    regels_incl.append(bereken_btw_over_bedrag(el, 21))
print(regels_incl)


# bedrag_exclusief = 63.15
# bedrag_inclusief = bereken_btw_over_bedrag(bedrag_exclusief, 21)

# print(bedrag_inclusief)