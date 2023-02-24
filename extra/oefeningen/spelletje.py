def mijn_functie():
    
    aantal_spellen = int(input("Hoeveel spellen wilt u? "))
    
    PRIJS_SPELLETJE = 24.95
    KORTING = 0.4
    extra = aantal_spellen * 0.25
    
    if aantal_spellen <2:
        som = PRIJS_SPELLETJE * (1 - KORTING)
        totaal = aantal_spellen * som
    else:
        som = PRIJS_SPELLETJE * (1 - KORTING) + extra
        totaal = aantal_spellen * som
        
    return totaal

print(f"Het kost €{mijn_functie()}.")