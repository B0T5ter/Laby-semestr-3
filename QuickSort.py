
def quickSort(l):
    if len(l) <= 1:
        return l
    
    pivot = l[-1]
    lewa = []
    prawa = []

    for x in l[:-1]:
        if x <= pivot:
            lewa.append(x)
        else:
            prawa.append(x)
    
    return quickSort(lewa) + [pivot] + quickSort(prawa)
    
l = [4,7,4,2,6,8,9]
print(quickSort(l))


