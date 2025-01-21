def euklides(a, b):
    if b == 0:
        return a
    return euklides(b, a % b)
a = 48
b = 18
print(euklides(a,b))