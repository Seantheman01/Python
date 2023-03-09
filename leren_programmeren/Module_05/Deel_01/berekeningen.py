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
    
# if choice == 'a':
#     n1 + n2
# elif choice == 'b':
#     n1 - n2
# elif choice == 'c':
#     n1 * n2
# elif choice == 'd':
#     n1 / n2
# elif choice == 'e':
#     n1 + n2
# elif choice == 'f':
#     n1 - n2
# elif choice == 'g':
#     n1 * n2
# elif choice == 'h':
#     n1 / n2 