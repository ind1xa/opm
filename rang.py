def podskupovi(myset, lek = True):
    l = list(myset)
    lists = [[]]
    for i in range(1, pow(2,len(l))):
        binstr = get_bin(i, len(l))
        sublist = []
        for j in range(0, len(l)):
            if binstr[j] == '1':
                sublist.append(l[j])
        if (lek == False):
            sublist.reverse()
        lists.append(sublist)
    return lists

def nClaniPodskup(myset, n, lek = True):
    svi = podskupovi(myset, lek)
    lists = []
    for x in svi:
        if len(x) == n:
            lists.append(x)
    return lists

def get_bin(x, n=0):
    return format(x, 'b').zfill(n)

def rang(mojskup, trazim, lek = True):
    svi = nClaniPodskup(mojskup, len(trazim), lek)
    svi.sort()
    counter = 0
    for skup in svi:
        presjek = trazim.intersection(skup)
        if (len(presjek) == len(trazim)):       #znaci da su isti
            break
        else:
            counter = counter + 1
    return 'Tvoj skup ima rang: ' + str(counter+1) + '.'

print(rang({1,2,3,4,5,6,7}, {2,4,5,7}, False))