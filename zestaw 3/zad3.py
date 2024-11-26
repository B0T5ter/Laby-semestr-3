def potega(a, b = None):
    if b == None:
        b = a
    if b == 1:
        return a
    return a * potega(a, b-1)

print(potega(3))