def mergeSort(l):

    if len(l) <= 1:
        return l
    
    n = len(l)//2
    lewa = mergeSort(l[:n])
    prawa = mergeSort(l[n:])

    ret = mergeConnect(lewa, prawa)

    return ret

def mergeConnect(l, p):
    ret = []
    while len(l) > 0 and len(p) > 0:
        if l[0] >= p[0]:
            ret.append(p[0])
            p.pop(0)
        else:
            ret.append(l[0])
            l.pop(0)
    for x in l:
        ret.append(x)

    for x in p:
        ret.append(x)

    return ret

l = [2,5,8,5,3,6,8]
print(mergeSort(l))

    
