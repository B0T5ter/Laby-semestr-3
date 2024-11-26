def tree(a):
    if a == 1:
        return "*"
    return a * "*" + '\n' + tree(a - 1)

print(tree(5))