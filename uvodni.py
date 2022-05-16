import collections

counter = 0

for x in range(10000, 100000):
    one = 0
    two = 0
    mystring = str(x)
    frequencies = collections.Counter(mystring)
    for key, value in frequencies.items():
        if key == '1': one = value
        if key == '2': two = value

    if ((one == 1 and two == 0) or (one == 0 and two == 1) or (one == 0 and two == 0)):
        counter += 1
    
    if one == 1 and two == 1:
        one = mystring.rfind("1")
        two = mystring.rfind("2")
        if one < two:
            counter += 1


print(counter)