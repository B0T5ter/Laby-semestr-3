def sum(a):
    if a < 10:
        return a
    return a%10 + sum(a//10)
print(sum(12))
