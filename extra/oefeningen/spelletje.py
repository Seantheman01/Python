def mijn_functie():
    
    aantal_spellen = int(input("Hoeveel spellen wilt u? "))
    
    PRIJS_SPELLETJE = 24.95
    korting = 0.4
    leveren = 1
    extra = aantal_spellen * 0.25
    
    if aantal_spellen <2:
        som = aantal_spellen * PRIJS_SPELLETJE * korting + leveren
    else:
        som = aantal_spellen * PRIJS_SPELLETJE * korting + leveren + extra
    
    return som

print(f"Het kost €{mijn_functie()}.")