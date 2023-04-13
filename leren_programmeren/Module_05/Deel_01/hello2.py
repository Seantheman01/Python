def mijn_functie(getal: int):
    mijn_string = ''
    
    for x in range(1, getal+1):
        mijn_string += f"Hello from function town {x}! \n" 
    return mijn_string
    
print(mijn_functie(7))