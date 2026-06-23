numeros = list(map(int, input().split()))

positivos = [i for i in numeros if i > 0]
print(positivos)