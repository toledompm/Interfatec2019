from functools import reduce

numProducts = int(input()) # quantidade de produtos a inserir

products = []

for product in range(numProducts):
    qty, price = input().split()
    products.append([int(qty), float(price)]) # [quantidade, preco]


total = reduce((lambda x, y: x[0] * x[1] + y[0] * y[1]), products)
print(total)