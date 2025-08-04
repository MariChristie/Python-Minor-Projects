# Gerador de boas-vindas.

# Crie um programa que pede ao usuário seu nome e depois o dá as boas-vindas dizendo "X seja bem-vindo", onde X é o nome do usuário.

nome = str(input("Escreva o seu nome: "))

if not nome:
    print("É só um espaço em branco.")
else: 
    print(f"Seja bem-vindo, {nome}")

