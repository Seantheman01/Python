def addition(number1, number2):
    return number1 + number2
    
def substraction(number1, number2):
    return number1 - number2
    
def multiplication(number1, number2):
    return number1 * number2
    
def division(number1, number2):
    return number1 / number2
   
choice = input("Wat wilt je doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? ")

if choice == 'a' or choice == 'b' or choice == 'c' or choice == 'd':
    n1 = int(input("Voer het eerste getal in: "))
    n2 = int(input("Voer het tweede getal in: "))

while True: 
        if choice == 'a':
            uitkomst = addition(n1, n2)
            print(f"{n1} + {n2} = {uitkomst}")
        elif choice == 'b':
            uitkomst = substraction(n1, n2)
            print(f"{n1} - {n2} = {uitkomst}")
        elif choice == 'c':
            uitkomst = multiplication(n1, n2)
            print(f"{n1} x {n2} = {uitkomst}")
        elif choice == 'd':
            uitkomst = division(n1, n2)
            print(f"{n1} : {n2} = {uitkomst}")
            
        elif choice == 'e' or choice == 'f':
            n1 = int(input("Voer een getal in: "))
            n2 = 1
            
            if choice == 'e':
                uitkomst = addition(n1, n2)
                print(f"{n1} + {n2} = {uitkomst}")
            elif choice == 'f':
                uitkomst = substraction(n1, n2)
                print(f"{n1} - {n2} = {uitkomst}")
            
        elif choice == 'g' or choice == 'h':
            n1 = int(input("Voer een getal in: "))
            n2 = 2

            if choice == 'g':
                uitkomst = multiplication(n1, n2)
                print(f"{n1} x {n2} = {uitkomst}")
            elif choice == 'h':
                uitkomst = division(n1, n2)
                print(f"{n1} : {n2} = {uitkomst}")
                    
        choice = input(f"Wil je wat met de uitkomst ({uitkomst}) doen? A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) niets? ")
        n1 = int(input("Voer een getal in: "))
        n2 = uitkomst
        
        if choice == 'i':
            break