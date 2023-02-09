import time

def fibo_efficient(lijst, lengte, start_tijd):
    if len(lijst) >= lengte:
        return(lijst)
    else:
        lijst.append(lijst[-1] + lijst[-2])
    return fibo_efficient(lijst, lengte)

lengte = 750
start_tijd = round(time.time() * 1000)
fibo_efficient([0, 1], 1000, start_tijd)
eind_tijd = round(time.time() * 1000)
print("eindtijd " + len(eind_tijd) + "begin " + "verschil " + eind_tijd - start_tijd)

start_tijd = round(time.time() * 1000)
fibo_n = [0, 1]
for x in range(lengte):
    fibo_n.append
eind_tijd = round(time.time() * 1000)
print(eind_tijd - start_tijd)