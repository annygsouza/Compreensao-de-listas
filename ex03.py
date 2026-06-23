def achatar(lista):
    final = []
    for item in lista:
        if type(item) == list:
            lista2 = achatar(item)
            for num in lista2:
                final.append(num)
        else:
            final.append(item)
    return final

inicial = eval(input())
print(achatar(inicial))

def achatar_plus(lista):
    return [a for a in lista if type(a) != list] + [b for item in lista if type(item) == list for b in achatar_plus(item)]

inicial = eval(input())
print(achatar_plus(inicial))