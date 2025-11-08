pedir = input("Digite seu CPF: ")
cpf_nove_digitos = pedir[0:9]
soma_digito1 = 0



if len(pedir) == 11:
    if len(set(pedir)) ==1:
        print("CPF inválido - todos os números iguais")
    else:
        for indice, digito in enumerate(cpf_nove_digitos):
            multiplicador = 10 - indice
            soma_digito1 += int(digito) * multiplicador
        resto = (soma_digito1 * 10) % 11
        if resto == 10:
            digito_calculado = 0
        else:
            digito_calculado = resto
        digito_original = int(pedir[9])
else: print("CPF inválido")

