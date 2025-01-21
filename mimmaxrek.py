l = [2,5,7,3,7,9]
def minMax(l, mini = None, maxi = None):
    if mini == None:
        mini = maxi = l[0]
    if l == []:
        return mini, maxi

    if mini > l[0]:
        mini = l[0]
    if maxi < l[0]:
        maxi = l[0]
    
    
    return minMax(l[1:], mini, maxi)
    

print(minMax(l))
