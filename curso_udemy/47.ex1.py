#Exercício
#Peça ao usuário para digitar seu nome
#Peça ao usuário para digitar sua idade
#Se o nome e idade forem digitados:

#Exiba mensagem:
#Seu nome é {nome}
#Seu nome invertido é {nome invertido}
#Seu nome contém (ou não) espaços
#Seu nome tem {n} letras
#A primeira letra do seu nome é {letra}
#A última letra do seu nome é {letra}

#Se nada for digitado em nome ou idade:
#Exiba: "Desculpe, você deixou campos vazios."

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Sua idade é {idade}")
    print(f"Seu nome invertido é {nome[::-1]}")
    contagem_espaços = nome.count(" ")
    print(f"Seu nome tem {contagem_espaços} espaços")
    total_letras = sum(1 for char in nome if char.isalpha())
    print(f"Seu nome tem {total_letras} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")

    