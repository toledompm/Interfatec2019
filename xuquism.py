altura,entradas = [int(i) for i in input().split()]
d = dict()
for i in range(entradas):
    chave,valor = input().split()
    d[chave] = valor

respostas = int(input())
resposta = 1
for i in range(respostas):
    r = bool(input().title())
    if r:
        resposta *= 2
    else:
        resposta = resposta * 2 + 1

print(d[str(resposta)])