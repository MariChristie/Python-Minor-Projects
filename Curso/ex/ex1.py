import string
from collections import Counter


frase = input("Digite uma frasse:").lower()
contagem = {}

for letra in frase:
    if letra in string.ascii_lowercase:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1 
print("\nContagem final:")
print(contagem)

#if .isalpha(frase):
