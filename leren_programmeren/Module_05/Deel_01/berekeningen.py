def addition(number1, number2):
    choice = int(input("Wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren?"))
    if choice == 'a' or choice == 'b' or choice == 'c' or choice == 'd':
        n1 = int(input("Typ het eerste getal in: "))
        n2 = int(input("Typ het tweede getal in: "))
    elif choice == 'e' or choice == 'f':
        n1 = int(input("Typ het eerste getal in: "))
        n2 = 1
    elif choice == 'g' or choice == 'h':
        n1 = int(input("Typ het eerste getal in: "))
        n2 = 2

choice = int(input(f"Wil je wat met de uitkomst () doen? A) iets optellen, B) iets aftrekken, C) met iets vermenigvuldigen, D) ergens door delen, E) ophogen, F) verlagen, G) verdubbelen, H) halveren of I) niets?"))