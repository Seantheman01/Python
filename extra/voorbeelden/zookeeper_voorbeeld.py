# opdracht 1:
giraf_aantal = int(input("Hoeveel giraffen zijn er? "))
struisvogel_aantal = int(input("Hoeveel struisvogels zijn er? "))
zebra_aantal = int(input("Hoeveel zebra's zijn er? "))

# giraf_aantal = 1
# struisvogel_aantal = 1
# zebra_aantal = 1

GIRAF_POTEN = 4
STRUISVOGEL_POTEN = 2
ZEBRA_POTEN = 4

def mijn_functie(giraffen, struisvogels, zebras):
    aantal_poten = giraf_aantal * GIRAF_POTEN + struisvogel_aantal * STRUISVOGEL_POTEN + zebra_aantal * ZEBRA_POTEN
    return aantal_poten

print(mijn_functie())
# print(mijn_functie(5,3,2)) dit mag
# print(mijn_functie(5,3,zebra_aantal)) dit mag ook
# print(giraf_aantal, struisvogel_aantal, zebra_aantal)) en dit ook


# -----------------------------------------------------------------


# opdracht 2:
tekst = """En ze stu[re]n [i]ngekleurde prentbriefkaarten van plekken waarvan ze zich niet 
reali[s]eren dat ze er nooit geweest zijn [a]an ' Iedereen op nummer 22, weer is prachti[g],
onz[e] kamer is aa[n]gekruisd. Missen jullie. E[t]en[ ]i[s] vettig , maar we hebben een geweldig
leuk restaurantje gevonden in de achterstraatjes waar ze Heine[ke]n hebben en kaas en uien
chips en iemand die "Een beetje verliefd" speel[t] op een a[c]cordeon ' en je zit vier dagen vast
op Schip[h]ol voor je vijfdaagse vliegvakantie met niks anders te eten dan uitgedroogde
voorverpakte boterhammen..."""

tussen_haakjes = ''
binnen_haakjes = False

for character in tekst:
    if binnen_haakjes and character != ']':
        tussen_haakjes += character
    elif character == '[':
        binnen_haakjes = True
    elif character == ']':
        binnen_haakjes = False
        
print(tussen_haakjes)