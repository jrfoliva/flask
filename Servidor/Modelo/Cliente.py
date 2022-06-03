
class Cliente(object):
    
    #Construtor da classe Cliente
    def __init__(self, nome, rg, cpf, dataNasc, cep="", rua="", num="", complemento="", bairro="", cidade="", estado="",
                    telefone="", email=""):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__dataNasc = dataNasc
        self.__cep = cep
        self.__rua = rua
        self.__num = num
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__telefone = telefone
        self.__email = email

    #método get
    @property
    def nome(self):
        return self.__nome
    
    #metodo setter
    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome
    

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, novoRg):
        self.__rg = novoRg
    

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novoCpf):
        self.__cpf = novoCpf

    
    @property
    def dataNasc(self):
        return self.__dataNasc
    
    @dataNasc.setter
    def dataNasc(self, novadataNasc):
        self.__dataNasc = novadataNasc

    
    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, novoCep):
        self.__cep = novoCep


    @property
    def rua(self):
        return self.__rua

    @rua.setter
    def rua(self, novaRua):
        self.__rua = novaRua
    

    @property
    def num(self):
        return self.__num
    
    @num.setter
    def num(self, novoNum):
        self.__num = novoNum


    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, novoComp):
        self.__complemento = novoComp

    

    @property
    def bairro(self):
        return self.__bairro
    
    @bairro.setter
    def bairro(self, novoBairro):
        self.__bairro = novoBairro

    
    @property
    def cidade(self):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, novaCidade):
        self.__cidade = novaCidade

    
    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, novoEstado):
        self.__estado = novoEstado


    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novoTel):
        self.__telefone = novoTel

    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, novoEmail):
        self.__email = novoEmail

    
    #sobrescrever o método str
    def __str__(self):
        return (f'Nome: {self.__nome}, RG: {self.__rg}, CPF: {self.__cpf}, Data Nasc.: {self.__dataNasc},\n'
            + f'Rua: {self.__rua}, N°: {self.__num}, Comp.: {self.__complemento}, Bairro: {self.__bairro},\n'
            + f'Cidade: {self.__cidade}, Estado: {self.__estado}, Tel.: {self.__telefone}\n'
            + f'Email: {self.__email}')

