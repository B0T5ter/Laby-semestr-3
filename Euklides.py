a = 12
b = 60

def euklides(a, b):
    if b == 0:
        return a
    return euklides(b, a%b)

print(euklides(a,b))
