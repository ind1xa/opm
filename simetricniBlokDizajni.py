
v = 13         #početni skup je veličine v, tolko ima i blokova
k = 4         #podskupovi su veličine k, svaka točka se nalazi u k blokova
alpha = 1     #svake dvije točke skupa v nalaze se istovremeno u alpha blokova
              #svaka dva bloka imaju alpha zajedničkih elemenata
t = 2


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

def jeRegularan(dizajn):
    for x in range(1, v+1):
        sum = 0
        for y in dizajn:
            sum += y.count(x)
            if (sum > k): return False
        if (sum != k): return False
    return True

def jeBalansiran(paroviIzV, dizajn):
    for x in paroviIzV:
        count = 0
        for y in dizajn:
            if set(x).issubset(y): 
                count += 1
                if (count > alpha): return False
        if (count != alpha): return False
    return True

def nijeRegularan(dizajn):
    for x in range(1, v+1):
        sum = 0
        for y in dizajn:
            sum += y.count(x)
            if (sum > k): 
                return True
        if (sum + (v - len(dizajn)) < k): 
            return True
    return False

def nijeBalansiran(paroviIzV, dizajn):
    for x in paroviIzV:
        count = 0
        for y in dizajn:
            if set(x).issubset(y): 
                count += 1
                if (count > alpha): return True
        if (count + (v - len(dizajn)) < alpha): return True
    return False

skup1 = {1}
for x in range(1, v+1):
    skup1.add(x)

kombinacije = nClaniPodskup(skup1,k)

skup2 = {1}
for x in range(1, len(kombinacije)+1):
    skup2.add(x)

paroviIzV = nClaniPodskup(skup1, t)

#moguciDizajni = nClaniPodskup(skup2,v)

moguciDizajn = []
indexPokusanih = v*[0]    

preskociSljedecuGranu = False

while (True):
    if (preskociSljedecuGranu):
        preskociSljedecuGranu = False
        while (True):
            moguciDizajn.pop()
            if (indexPokusanih[len(moguciDizajn)] < len(kombinacije)-(v-len(moguciDizajn))):
                moguciDizajn.append(kombinacije[indexPokusanih[len(moguciDizajn)]])
                break
        for x in range(len(moguciDizajn), len(indexPokusanih)):
            indexPokusanih[x] = indexPokusanih[len(moguciDizajn)-1]-len(moguciDizajn)+x
    else:
        moguciDizajn.append(kombinacije[indexPokusanih[len(moguciDizajn)]])
    if (indexPokusanih[len(moguciDizajn)-1]+1 < len(kombinacije)-(v-len(moguciDizajn))):
        indexPokusanih[len(moguciDizajn)-1] += 1
        for x in range(len(moguciDizajn), len(indexPokusanih)):
            indexPokusanih[x] = indexPokusanih[len(moguciDizajn)-1]-len(moguciDizajn)+x
    else:
        preskociSljedecuGranu = True;
    if (nijeRegularan(moguciDizajn) or nijeBalansiran(paroviIzV, moguciDizajn)):
        moguciDizajn.pop()
    if (len(moguciDizajn) == v):
        if (jeRegularan(moguciDizajn) and jeBalansiran(paroviIzV, moguciDizajn)):
            print("Simetrični v = " + str(v) + ", k = " + str(k) + ", alpha = " + str(alpha) + " dizajn je: ")
            print(moguciDizajn)
            break
        moguciDizajn.pop()

