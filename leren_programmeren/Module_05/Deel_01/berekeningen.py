def addition(number1, number2):
    return number1 + number2
    
def substraction(number1, number2):
    return number1 - number2
    
def multiplication(number1, number2):
    return number1 * number2
    
def division(number1, number2):
    return number1 / number2
   
choice = input("Wat wilt je doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? ")
n1 = int(input("Voer het eerste getal in: "))

# if choice == 'a' or choice == 'b' or choice == 'c' or choice == 'd':
#     n2 = int(input("Voer het tweede getal in: "))
    
while True:
    if choice == 'a':
        n2 = int(input("Voer het tweede getal in: "))
        uitkomst = addition(n1, n2)
        print(f"{n1} + {n2} = {uitkomst}")
    elif choice == 'b':
        n2 = int(input("Voer het tweede getal in: "))
        uitkomst = substraction(n1, n2)
        print(f"{n1} - {n2} = {uitkomst}")
    elif choice == 'c':
        n2 = int(input("Voer het tweede getal in: "))
        uitkomst = multiplication(n1, n2)
        print(f"{n1} x {n2} = {uitkomst}")
    elif choice == 'd':
        n2 = int(input("Voer het tweede getal in: "))
        uitkomst = division(n1, n2)
        print(f"{n1} : {n2} = {uitkomst}")
        
    # elif choice == 'e' or choice == 'f':
    #     n1 = int(input("Voer een getal in: "))
    #     n2 = 1
        
    if choice == 'e':
        n2 = 1
        uitkomst = addition(n1, n2)
        print(f"{n1} + {n2} = {uitkomst}")
    elif choice == 'f':
        n2 = 1
        uitkomst = substraction(n1, n2)
        print(f"{n1} - {n2} = {uitkomst}")
        
    # elif choice == 'g' or choice == 'h':
    #     n1 = int(input("Voer een getal in: "))
    #     n2 = 2

    if choice == 'g':
        n2 = 2
        uitkomst = multiplication(n1, n2)
        print(f"{n1} x {n2} = {uitkomst}")
    elif choice == 'h':
        n2 = 2
        uitkomst = division(n1, n2)
        print(f"{n1} : {n2} = {uitkomst}")
                
    choice = input(f"Wil je wat met de uitkomst ({uitkomst}) doen? A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) niets? ")
    if choice == 'a' or choice == 'b' or choice == 'c' or choice == 'd':
        n1 = uitkomst
    elif choice == 'e' or choice == 'f' or choice == 'g' or choice == 'h':
        n1 = uitkomst
    elif choice == 'i':
        break