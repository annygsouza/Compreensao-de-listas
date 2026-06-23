matriz = eval(input())  
num = sum(matriz, [])

pares = [i for i in num if i % 2 == 0]
print(pares)