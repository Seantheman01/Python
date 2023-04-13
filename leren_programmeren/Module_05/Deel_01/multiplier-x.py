def mijn_functie(som: int):
    mijn_string = ''
    
    for x in range(1, 11):
        mijn_string += f"{x} x {som} = {x * som} \n"
    return mijn_string
        
print(mijn_functie(3))