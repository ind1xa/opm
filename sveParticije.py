
#Broj particija od m u n dijelova jednak je broju particija od m 
#  kojima je najveći dio n. Taj broj ćemo označavati s P(m,n).


def sveParticije(broj):
    finlista = []
    for x in range(0, broj):
        particije = []
        particije.append(broj-x)
        if (x != 0):
            smth = sveParticije(x)
        else: 
            smth = []
            finlista.append(particije)
        #print (smth)
        for y in smth:
            if (max(y) <= broj-x): 
                particije2 = particije.copy()
                particije2.extend(y)
                finlista.append(particije2)
    return finlista
        
def dvaParDvaNe(lista):
    counterPar = 0
    counterNe = 0
    for x in lista:
        if (x%2==0): counterPar = counterPar+1
        if (x%2==1): counterNe = counterNe+1
    if (counterPar == counterNe == 2): return True
    return False

def baremJedanParan(lista):
    for x in lista:
        if (x%2==0): return True
    return False

counter = 0

print(len(sveParticije(30)))


#print(sve)


