def primos(limit,start):
    crivo_lista = list()
    crivo_lista.append(0)
    crivo_lista.append(0)
    for i in range(limit-1):
        crivo_lista.append(1)
    for i in range(int(limit**0.5)+1):
        if crivo_lista[i] == 1:
            for x in range(i**2,limit+1,i):
                crivo_lista[x] = 0
    primos = list()
    for i in range(start,(limit+1)):
        if crivo_lista[y] == 1:
            primos.append(y)
    return primos

intervalos = int(input())

for i in range(intervalos):
    count_ocorrencias = [0,0,0,0,0,0,0,0,0,0]
    start,limit = [int(x) for x in input().split()]
    primos_intervalo = primos(limit,start)
    for x in range(len(primos_intervalo)):
        for z in str(primos_intervalo[x]):
            count_ocorrencias[int(z)] += 1
    print('INTERVALO {}'.format(i+1))
    for y in range(10):
        print('{}: {}'.format(y,count_ocorrencias[y]))
