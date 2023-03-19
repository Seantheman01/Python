def addition(number1, number2):
    print(number1 + number2)
    
def substraction(number1, number2):
    print(number1 - number2)
    
def multiplication(number1, number2):
    print(number1 * number2)
    
def division(number1, number2):
    print(number1 / number2)
   
choice = input("Wat wilt je doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? ")

while True: 
    if choice == 'a' or choice == 'b' or choice == 'c' or choice == 'd':
        n1 = int(input("Voer het eerste getal in: "))
        n2 = int(input("Voer het tweede getal in: "))
        
        if choice == 'a':
            uitkomst = addition(n1, n2)
        elif choice == 'b':
            uitkomst = substraction(n1, n2)
        elif choice == 'c':
            uitkomst = multiplication(n1, n2)
        elif choice == 'd':
            uitkomst = division(n1, n2)
            
    elif choice == 'e' or choice == 'f':
        n1 = int(input("Voer een getal in: "))
        n2 = 1
        print(n2)
        
        if choice == 'e':
            uitkomst = addition(n1, n2)
        elif choice == 'f':
            uitkomst = substraction(n1, n2)
        
    elif choice == 'g' or choice == 'h':
        n1 = int(input("Voer een getal in: "))
        n2 = 2
        print(n2)

        if choice == 'g':
            uitkomst = multiplication(n1, n2)
        elif choice == 'h':
            uitkomst = division(n1, n2)
                
    choice = input(f"Wil je wat met de uitkomst ({uitkomst}) doen? A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) niets? ")