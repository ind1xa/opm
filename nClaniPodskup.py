def nClaniPodskup(myset, n):                #kombinacije bez ponavljanja
    lists = []
    pocetniSkup = list(myset)
    pocetniSkup.sort()
    podskup = []
    for x in range (0, n):
        podskup.append(pocetniSkup[x])
    lists.append(podskup)
    while(True):
        podskup = dohvatiSljedeciPodskup(pocetniSkup, podskup).copy()
        if (len(podskup) == 0): 
            break
        lists.append(podskup)
    return lists
    
def dohvatiSljedeciPodskup(veci, manji):
    mojManji = manji.copy()
    veci.sort()
    mojManji.sort()
    for x in range(1, len(mojManji)+1):
        indexUVecem = veci.index(mojManji[len(mojManji)-x])
        if (indexUVecem < (len(veci)-x)):
            for y in range(0, x):
                mojManji[len(mojManji)-x+y] = veci[indexUVecem+1+y]
            return mojManji
    return []


print(nClaniPodskup({1,2,3,4,5},3))