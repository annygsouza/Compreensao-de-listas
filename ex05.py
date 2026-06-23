nomes = input().split()

filtrados = [i for i in nomes if len(i) > 5]
print(filtrados)