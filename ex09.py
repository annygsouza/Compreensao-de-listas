def primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False  
    return True

n = int(input())
primos = [x for x in range(n + 1) if primo(x)]

print(primos)