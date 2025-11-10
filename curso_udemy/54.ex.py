"""""
Faça um programa que peça ao usuário um número inteiro, 
Informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

pedir = input("Digite um número inteiro: ")

if pedir.lstrip('-').isdigit():
    numero = int(pedir)
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
else:
    print("Isso não é um número inteiro.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex: 
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.
"""

pedir_hora = input("Digite a hora atual (0-23): ")

try:
    pedir_hora.isdigit()
    
    hora = int(pedir_hora)
    if hora in range(0, 12):
        print("Bom dia!")
    elif hora in range(10, 17):
        print("Boa tarde!")
    elif hora in range(18, 23):
        print("Boa noite!")
except:
    print("Por favor, digite um número válido entre 0 e 23.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos, escreva "Seu nome é curto"; se tiver entre 5 a 6 letras, escreva
"Seu nome é normal"; maior que 6, escreva "Seu nome é muito grande".
"""

nome = input("Digite seu primeiro nome: ")

for char in nome:
    if char.isalpha():
        tamanho_nome = len(nome)
        if tamanho_nome in range (0, 4):
            print("Seu nome é curto.")
        elif tamanho_nome in range(5, 6):
            print("Seu nome é normal")
        else: 
            print("Seu nome é muito grande.")
        break
else: 
    print("Por favor, digite um nome válido.")