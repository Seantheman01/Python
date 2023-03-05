nummer = 10

def fibonacci(x):
    if x <= 1:
        return x
    else:
        return (fibonacci(x - 1) + fibonacci(x - 2))
    
if nummer > 0:
    for y in range(nummer):
        print(fibonacci(y))