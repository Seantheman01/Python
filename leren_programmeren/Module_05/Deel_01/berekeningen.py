def addition(number1, number2):
    print(number1 + number2)
    
def substraction(number1, number2):
    print(number1 - number2)
    
def multiplication(number1, number2):
    print(number1 * number2)
    
def division(number1, number2):
    print(number1 / number2)
    
addition(2,1)
substraction(2,1)
multiplication(2,1)
division(2,1)

choice = input("Wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? ")
if choice == 'a' or choice == 'b' or choice == 'c' or choice == 'd':
    n1 = int(input("Voer het eerste getal in: "))
    n2 = int(input("Voer het tweede getal in: "))
elif choice == 'e' or choice == 'f':
    n1 = int(input("Voer een getal in: "))
    n2 = 1
elif choice == 'g' or choice == 'h':
    n1 = int(input("Voer een getal in: "))
    n2 = 2