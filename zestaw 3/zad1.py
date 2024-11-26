def rekBin(a):
    if a == 1:
        return 1
    if a == 0:
        return 0
    else:
        return  str(rekBin(a//2)) + str(a%2)
    
print(rekBin(100))