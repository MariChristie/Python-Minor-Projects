#Crie um programa que recebe dois valores e exibe qual é o maior entre eles.

valor_1 = int(input("Digite um valor: "))
valor_2 = int(input("Digite outro valor: "))

if valor_1 > valor_2:
    print("Valor 1 é maior.")
elif valor_1 == valor_2 :
    print("Os valores são iguais")
else:
    print("Valor 2 é maior")
