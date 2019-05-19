carros = int(input())
menorEntrada = 24*60
maiorSaida = -1*60
for i in range(carros):
    temp = [int(i) for i in input().split()]
    entrada = temp[0]*60 + temp[1]
    saida = temp[2]*60 + temp[3]
    if entrada < menorEntrada:
        menorEntrada = entrada
    if saida > maiorSaida:
        maiorSaida = saida

print(maiorSaida-menorEntrada)