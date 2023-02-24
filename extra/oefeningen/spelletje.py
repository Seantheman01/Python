def mijn_functie():
    
    aantal_spellen = int(input("Hoeveel spellen wilt u? "))
    SPELLETJE = 24.95
    korting = 0.4
    leveren = 1
    extra = 0.25    
    
    if aantal_spellen <2:
        som = aantal_spellen * SPELLETJE * korting + leveren
    elif aantal_spellen >=2:
        som = aantal_spellen * SPELLETJE * korting + leveren + extra
    
    return som

print(mijn_functie())