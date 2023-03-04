def fibonacci(x):
    # teller = 0
    # while teller <= x:
        if x in {0, 1}:
            return x
        return fibonacci(x - 1) + fibonacci(x - 2)
    
