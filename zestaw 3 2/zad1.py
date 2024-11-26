def bin(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    return f'{a%2}' + f'{bin(a//2)}'

print(bin(5)) 
        