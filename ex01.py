def ler_num():
    num = input().split()
    return [int(n) for n in num]

print(ler_num())