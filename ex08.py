numeros = list(map(int, input().split()))

pares = [i for i in numeros if i % 2 == 0]
print(pares)