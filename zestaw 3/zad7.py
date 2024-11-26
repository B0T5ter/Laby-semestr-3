def a(x):
    ret = 0
    for x in range(x):
        if x != 0:
            ret += (1/x)

    return ret

def b(x):
    ret = 0
    for x in range(x):
        if x != 0:
            ret += (1/x**2)

    return ret

def c(x):
    ret = 0
    for x in range(x):
        ret += x

    return ret

def d(x):
    ret = 0
    for x in range(x):
        ret += (2**x)

    return ret

def e(x):
    ret = 0
    for x in range(x):
        ret += (x*(x + 1) * (x + 2)/ 6)

    return ret

print(a(10))
print(b(10))
print(c(10))
print(d(10))
print(e(10))