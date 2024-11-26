def potega(a, n = None):
    if n == 0:
        return a
    return a * (potega(a, n-1))

print(potega(3,3))