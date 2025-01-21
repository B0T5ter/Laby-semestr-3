licz = 15
stop = 2
epsilon = 0.0001
def square(kon, stop, epsilon, pocz = 0):
    srodek = (pocz + kon)/2
    aktualny = srodek**stop
    #|print(aktualny, licz)
    if aktualny <= licz + epsilon and aktualny >= licz - epsilon:
        return srodek
    elif srodek**stop > licz:
        return square(srodek, stop, epsilon, pocz)
    else:
        return square(kon, stop, epsilon, srodek)
    

print(square(licz, stop, epsilon))