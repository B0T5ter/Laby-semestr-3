def sumCy(a):
    if a < 10:
        return a
    return a%10 + sumCy(a//10)

print(sumCy(3213))