def fib(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    return fib(a - 1) + fib(a - 2)

print(fib(10))
for x in range(10):
    print(fib(x))