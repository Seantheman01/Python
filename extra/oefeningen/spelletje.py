aantal_spellen = int(input("Hoeveel spellen wilt u? "))

PRIJS_SPELLETJE = 24.95
KORTING = 0.4

def mijn_functie():    
    
    som = PRIJS_SPELLETJE * (1 - KORTING)
    totaal_prijs = aantal_spellen * som

    print(f"Het kost €{str(totaal_prijs)}.")
    print(totaal_prijs)

    verzendkosten = 1 + ((aantal_spellen - 1) * 0.25)
    
    return verzendkosten + totaal_prijs

print(mijn_functie())