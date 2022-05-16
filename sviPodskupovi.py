
def sviPodskupovi(myset):
    l = list(myset)
    lists = [[]]
    for i in range(1, pow(2,len(l))):
        binstr = get_bin(i, len(l))
        sublist = []
        for j in range(0, len(l)):
            if binstr[j] == '1':
                sublist.append(l[j])
        lists.append(sublist)
    return lists

def get_bin(x, n=0):
    return format(x, 'b').zfill(n)

S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
for x in range(12, 26):
    S.add(x)
svi = sviPodskupovi(S)
print(S)
counter = 0
for x in svi:
    suma = 0
    for y in x:
        suma = suma + y
    if (suma == 50):
        #print(x)
        counter = counter +1

print(counter)