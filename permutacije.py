import time
start_time = time.time()


def svePermutacije(n):                      #bijekcije
    rezultat = []
    skup = []
    for x in range (1, n+1):
        skup.append(x)
    rezultat.append(skup)
    while(True):
        skup = sljPermutacija(skup)
        if(len(skup) == 0):
            break;
        rezultat.append(skup)
    return rezultat

def sljPermutacija(prosli):
    skup = prosli.copy()
    tail = []
    for x in range(1, len(prosli) + 1):
        tail.append(prosli[len(prosli)-x])
        if not(prosli[len(prosli)-x] < prosli[len(prosli)-1-x]):
            tail.append(skup[len(prosli)-1-x])
            sljMax = sljedeciNajveci(skup, skup[len(prosli)-1-x])
            if (sljMax == -1): break
            skup[len(prosli)-1-x] = sljMax
            tail.remove(sljMax)
            tail.sort()
            for y in range (len(prosli)-x, len(prosli)):
                skup[y] = tail[y-len(prosli)+x]
            return skup
    return []

def sljedeciNajveci(skup, n):
    index = skup.index(n)
    podskup = []
    for y in range (0,index):
        podskup.append(skup[y])
    for x in range (n+1, len(skup)+1):
        if (podskup.count(x) == 0): return x
    return -1


print(sljPermutacija([4,1,6,8,7,10,9,5,3,2]))
    
        
print("--- %s seconds ---" % (time.time() - start_time))