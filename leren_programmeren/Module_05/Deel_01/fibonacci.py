def fibonacci(x):
    a = 0
    b = 1
    
    if x == 0:
        return a
    elif x == 1:
        return b
    else:
        return fibonacci(x-1) + fibonacci(x-2)
            
print(fibonacci)