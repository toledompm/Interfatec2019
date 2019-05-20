def crivo(l,s):
    c = list()
    c.append(0)
    c.append(0)
    for z in range(l-1):
        c.append(1)
    for i in range(int(l**0.5)+1):
        if c[i] == 1:
            for x in range(i**2,l+1,i):
                c[x] = 0
    primos = list()
    for y in range(s,(l+1)):
        if c[y] == 1:
            primos.append(y)
    return primos

intervalos = int(input())

for i in range(intervalos):
    d = [0,0,0,0,0,0,0,0,0,0]
    sta,lim = [int(x) for x in input().split()]
    my_crivo = crivo(lim,sta)
    for x in range(len(my_crivo)):
        for z in str(my_crivo[x]):
            d[int(z)] += 1
    print('INTERVALO {}'.format(i+1))
    for y in range(10):
        print('{}: {}'.format(y,d[y]))
