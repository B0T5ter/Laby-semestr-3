l = [2,3,5]
key = 2

def hommerItera(l, key):
    ret = l[0]
    for x in range(1, len(l)):
        ret = ret * key + l[x]

    return ret

def hommerRek(l, key):
    if len(l) == 1:
        return l[0]
    return l[0] + key * hommerRek(l[1:], key)

print(hommerItera(l, key))
print(hommerRek(l, key))

