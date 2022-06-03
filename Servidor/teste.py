
from Modelo.Pet import Pet
from Persistencia.PetBD import PetBD
from Modelo.Cliente import Cliente
from Persistencia.ClienteBD import ClienteBD


# cria uma instância de Pet

# meuPet = Pet('','simba', 'canina', 'york', 'branca', '01/12/2019', '1000-', '12347')
# petdb  = PetBD()
# petdb.incluir(meuPet)
#
# resposta = petdb.consultar('%')
# if isinstance(resposta, list):
#     for item in resposta:
#         print(item)
# else:
#     print(resposta)


# instanciando um cliente
cli1 = Cliente("Veruska", "12313134", "328.562.438-86", "1979-12-19", "19065540",
   "Aristóteles Martins", "83", "", "Jardim Balneário", "Presidente Prudente", "SP",
   "(18) 99806-7041", "teste@teste")
# cli2 = Cliente("Maria Aparecida", "1024554212", "32856243886", "09/11/1956", "19065-540",
#   "Ernesto Brogiato", "28", "", "CECAP", "Presidente Prudente", "SP",
#    "(18) 9999-9911", "teste@teste")

cliBD = ClienteBD()
cliBD.incluir(cli1)

# cliBD.alterar(cli1)
#cliBD.apagar(cli2)

resposta = cliBD.consultar("")
if isinstance(resposta, list):
    for cliente in resposta:
        print(cliente)
        print(80*'-')
else:
    print(resposta)
