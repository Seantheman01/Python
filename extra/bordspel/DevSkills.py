import random
from dobbelstenen import DOBBELSTENEN

# rol dobbelsteen
dobbelsteen = random.choice(DOBBELSTENEN)
print(dobbelsteen)

if dobbelsteen == DOBBELSTENEN[1]:
    print("Nee")