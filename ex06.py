def quant_vogais(txt):
    return sum ([1 for i in txt if i in 'aeiouAEIOU'])

texto = input()
print(quant_vogais(texto))