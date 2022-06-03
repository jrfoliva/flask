"""
    Funções para validação de campos do formulário de clientes
"""

def calculaDigito(cpf, mult):
    soma = 0
    dig = 0
    for i in range(len(cpf)):
        if cpf[i] not in ['.', '-']:
            soma += int(cpf[i]) * mult
            mult -= 1
    resto = soma % 11
    if resto < 2:
        dig = 0
    elif resto >= 2:
        dig = 11 - resto
    return str(dig)


def validarCPF(cpf):
    ok = False
    #if (len(cpf) == 14) and (cpf[3] == ".") and (cpf[7] == ".") and (cpf[11] == "-"):
    if (calculaDigito(cpf[0:11], 10) == cpf[12] and calculaDigito(cpf[0:13], 11) == cpf[13]):
        ok = True
    return ok


def validaDadosCliente(dados):
    for campo, valor in dados.items():
        print(f'{campo}: {valor}')
    teste = True
    if dados['nome'].isdigit():
        teste = False
    elif not dados['rg'].isdigit():
        teste = False
    elif not validarCPF(dados['cpf']):
        teste = False
    return teste

