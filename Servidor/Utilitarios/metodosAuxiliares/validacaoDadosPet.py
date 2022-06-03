"""
    Módulo que será utilizados para métodos de validação dos campos recebidos do forumlário
"""
def validaDadosPet(dados):
    """Método que verifica se há campos vazios."""
    for k, v in dados.items():
        print(f'{k} : {v}')
        
    teste = True
    if dados['nomePet'].isdigit():
        teste = False
    elif dados['especiePet'].upper() not in ['CANINA', 'FELINA', 'EQUINA', 'BOVINA', 'AVE']:
        teste = False
    elif dados['racaPet'].isdigit():
        teste = False
    elif dados['corPet'].isdigit():
        teste = False
    return teste

# teste = {"nomePet": "Fred", "especiePet": "Canina", "racaPet": "Vira-Lata", "corPet": "Branca"}
# print(validaDadosPet(teste))