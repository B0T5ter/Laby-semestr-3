def a(x):
    if x == 1:
        return 1
    return 1/x + a(x-1)

def b(x):
    if x == 1:
        return 1
    return 1/x**2 + b(x-1)

def c(x):
    if x == 1:
        return 1
    return x + c(x - 1)

def d(x):
    if x == 1:
        return 1
    return 2**x + d(x - 1)

def e(x):
    if x == 1:
        return 1
    return (x * (x + 1) * (2 * x + 1))/(6) + e(x - 1)

print(a(5))
print(b(5))
print(c(5))
print(d(5))
print(e(5))
