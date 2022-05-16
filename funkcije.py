from itertools import count
from re import I

import time
start_time = time.time()


def sveFunkcije(iz, u):         #rezultat nam govori u koju točku se svaka od početnih točaka preslikala
    rezultat = []               #varijacije s ponavljanjem, pred i blag mogu biti ista osoba
    fja = []
    for x in range (0, iz):
        fja.append(1)
    rezultat.append(fja)
    while(True):
        fja = dohvatiSljFju(fja, u)
        if (len(fja) == 0): 
            break
        rezultat.append(fja)
    
    return rezultat

def dohvatiSljFju(prethodna, n):
    nova = prethodna.copy()
    for x in range (0, len(prethodna)):
        if (nova[len(prethodna)-1-x]+1 <= n):
            nova[len(nova)-1-x] = nova[len(nova)-1-x] +1
            for y in range (len(prethodna)-x, len(prethodna)):
                nova[y] = 1
            return nova
    return []
    
#------------------------------------------------------------

def sveInjekcije(iz, u):                #varijacije bez ponavljanja, biranje predsjednika i blagajnika u razredu
    rezultat = []
    fja = []
    for x in range (1, iz+1):
        fja.append(x)
    rezultat.append(fja)
    while(True):
        fja = dohvatiSljInjek(fja, u)
        if (len(fja) == 0): 
            break
        rezultat.append(fja)
    
    return rezultat

def dohvatiSljInjek(prethodna, n):
    nova = prethodna.copy()
    broj = 0
    for x in range (0, len(prethodna)):
        broj = moguPovecatNa(prethodna, len(prethodna)-1-x, n)
        if (broj != -1):
            nova[len(nova)-1-x] = broj
            for y in range (len(prethodna)-x, len(prethodna)):
                povecanje = moguPovecatNa(nova, y, n, True)
                if (povecanje == -1): return []
                nova[y] = povecanje
            return nova
    return []

def moguPovecatNa(prethodnaFja, index, n, kreniOd0 = False):
    fjaZaBrojanje = []
    prethodna = prethodnaFja.copy()
    if (kreniOd0): prethodna[index] = 0;
    for x in range (0, index):
        fjaZaBrojanje.append(prethodna[x])
    i = 1
    while (prethodna[index] + i <= n):
        if (fjaZaBrojanje.count(prethodna[index] + i) == 0):
            return prethodna[index] + i
        i = i +1
    return -1

#----------------------------------------------------

def strogoRastuceFje(iz, u):                            #kombinacije bez ponavljanja
    rezultat = []                                       #loto
    fja = []
    for x in range(1, iz+1):
        fja.append(x)
    rezultat.append(fja)
    while(True):
        fja = dohvatiSljStRast(fja, u)
        if (len(fja) == 0): 
            break
        rezultat.append(fja)
    
    return rezultat

def dohvatiSljStRast(skup, max):
    sljStRast = skup.copy()
    for x in range(0, len(skup)):
        broj = skup[len(skup)-1-x]
        if (broj +1 <= max - x):
            sljStRast[len(skup)-1-x] = broj + 1
            for y in range (len(skup)-x, len(skup)):
                sljStRast[y] = broj+1+(y-len(skup)+x+1)
            return sljStRast
    return[]

#-------------------------------------

def rastuceFje(iz, u):                      #kombinacije s ponavljanjem
    rezultat = []                           #loto s vraćanjem kuglica u bubanj
    fja = []
    for x in range(1, iz+1):
        fja.append(1)
    rezultat.append(fja)
    while(True):
        fja = dohvatiSljRast(fja, u)
        if (len(fja) == 0): 
            break
        rezultat.append(fja)
    return rezultat

def dohvatiSljRast(skup, max):
    sljRast = skup.copy()
    for x in range(0, len(skup)):
        broj = skup[len(skup)-1-x]
        if (broj +1 <= max):
            sljRast[len(skup)-1-x] = broj + 1
            changeHappened = False
            for y in range (len(skup)-x, len(skup)):
                if (sljRast[y] != broj+1): 
                    changeHappened = True
                sljRast[y] = broj+1
            return sljRast
    return[]

#------------------------------------------

def sveSurjekcije(iz, u):       #trcat po svima i filtrirat surjekcije
    rezultat = []
    fja = []
    for x in range (0, iz-u):
        fja.append(1)
    for x in range (1, u+1):
        fja.append(x)
    rezultat.append(fja)
    while(True):
        fja = dohvatiSljFju(fja, u)
        if (len(fja) == 0): 
            break
        if (je2Surjekcija(fja, u)):
            print(fja)
            rezultat.append(fja)
    return rezultat

def jeSurjekcija(skup, max):
    for x in range (1, max+1):
        if (skup.count(x) == 0):
            return False
    return True

def je2Surjekcija(skup, max):
    for x in range (1, max+1):
        if (skup.count(x) < 2):
            return False
    return True


print(len(sveSurjekcije(14,5)))


print("--- %s seconds ---" % (time.time() - start_time))