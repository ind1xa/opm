from time import sleep


lista = [-1]*6
counter = 0
def svaRjesenja(brXova, rez):
    global counter
    if (brXova == 1):
        lista[len(lista)-1] = rez
        #print(lista)
        counter = counter+1
    else: 
        for x in range (0, rez+1):
            lista[len(lista)-brXova] = x
            svaRjesenja(brXova-1, rez-x)


svaRjesenja(6,17)
print(counter)