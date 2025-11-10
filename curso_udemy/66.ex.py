""" Calculadora com while"""

while True:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    operador = input("Digite o operador (+-*/): ")

    numeros_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos os números são inválidos.")
        continue

    operadores_permitidos = "+-*/"
    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    ########
    sair = input("Desejar sair? [s]sim): ").lower().startswith('s')
    print(sair)

    if sair is True:
        break