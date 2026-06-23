notas = list(map(float, input().strip("[]").split()))
acima_media = [nota for nota in notas if nota > 5]

print(len(acima_media))