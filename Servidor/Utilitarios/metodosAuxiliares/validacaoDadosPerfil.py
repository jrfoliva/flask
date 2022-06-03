def validaDadosPerfil(dados):
    valido = True
    if dados['perfil'].isdigit():
        valido = False
    elif dados['consultar']  == "1":
        dados['consutar'] = int(dados['consultar'])
    elif dados['incluir']  == "1":
        dados['incluir'] = int(dados['incluir'])
    elif dados['alterar']  == "1":
        dados['alterar'] = int(dados['alterar'])
    elif dados['excluir']  == "1":
        dados['excluir'] = int(dados['excluir'])
    return valido
    