"""
Iterando strings com while
"""

#------ 012345678910 ------
#------ 1110987654321 ------


"""nome = input("Digite seu nome e sobrenome: ")
sim = "*"
nova_string = ""

for nome in nome:
    nova_string = nova_string + nome + sim
print(nova_string)"""
    

nome = input("Digite seu nome e sobrenome: ")
indice = 0
novo_nome = ""

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)