import random; arr = [random.randint(0, 100) for _ in range(10)]
arr = [3, 1, 2, 4, 3]
def tape(arr):
    lewa = 0
    prawa = sum(arr)
    roz = prawa
    for x in range(len(arr)):
        lewa += arr[x]
        prawa -= arr[x]
        if abs(prawa - lewa) < roz:
            roz = abs(prawa - lewa)
    return roz

print(tape(arr))