def addition(number1, number2):
    print(number1 + number2)
    
def substraction(number1, number2):
    print(number1 - number2)
    
def multiplication(number1, number2):
    print(number1 * number2)
    
def division(number1, number2):
    print(number1 / number2)
    
choice = input("Wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? ")

n1 = int(input("Voer het eerste getal in: "))
n2 = int(input("Voer het tweede getal in: "))

if choice == 'a':
    n1 + n2
elif choice == 'b':
    n1 - n2
elif choice == 'c':
    n1 * n2
elif choice == 'd':
    n1 / n2
elif choice == 'e':
    n1 + 1
elif choice == 'f':
    n1 - 1
elif choice == 'g':
    n1 * 2
elif choice == 'h':
    n1 / 2