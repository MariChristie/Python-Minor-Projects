"""
Objetivo: Escrever um programa onde o computador "pensa" em um número secreto, e 
o usuário tem que continuar adivinhando até acertar. O programa deve dar dicas se o 
palpite foi muito alto ou muito baixo.
"""
import random

numero_aleatorio = random.randint(1, 10)

print("Adivinhe um número de 1 a 10.")

while True: 
    adivinhar = input("Digite umm valor: ")
    if adivinhar.isdigit():
        palpite_numero = int(adivinhar)
        if palpite_numero == numero_aleatorio:
            print("O número está certo.")
            break
        elif palpite_numero > numero_aleatorio:
            print("O número está longe")
        else:
            palpite_numero < numero_aleatorio
            print("O número está perto")
    else:
        print("Não é um número.")