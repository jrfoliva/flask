
class Usuario(object):
    
    def __init__(self, nome, rg, cpf, dtNasc, cep, endereco, complemento, numero, bairro, cidade,
                estado, email, numTelefone, login, senha, perfil, ativo):
        self.__nome = nome
        self.__rg = rg
        self.__cpf = cpf
        self.__dtNasc = dtNasc
        self.__cep = cep
        self.__endereco = endereco
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__email = email
        self.__numTelefone = numTelefone
        self.__login = login
        self.__senha = senha
        self.__perfil = perfil
        self.__ativo = ativo


    
    #métodos get
    @property
    def nome(self):
        return self.__nome

    #métodos set
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
    def dtNasc(self):
        return self.__dtNasc

    @dtNasc.setter
    def dtNasc(self, novadtNasc):
        self.__dtNasc = novadtNasc
    
    
    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, novoCep):
        self.__cep = novoCep


    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, novoEnd):
        self.__endereco = novoEnd

    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, novoNum):
        self.__numero = novoNum
    

    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, novoComplemento):
        self.__complemento = novoComplemento


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
    def email(self):
        return self.__email

    @email.setter
    def email(self, novoEmail):
        self.__email = novoEmail

    
    @property
    def numTelefone(self):
        return self.__numTelefone
    
    @numTelefone.setter
    def numTelefone(self, novoNum):
        self.__numTelefone = novoNum


    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, novoLogin):
        self.__login = novoLogin
    

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, novaSenha):
        self.__senha = novaSenha


    @property
    def perfil(self):
        return self.__perfil

    @perfil.setter
    def perfil(self, novoPerfil):
        self.__perfil = novoPerfil

    
    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, novoAtivo):
        self.__ativo = novoAtivo


# user = Usuario('Junior', '30.105.503-8', '215.885.528-29', '1980-02-04',
#     '19065-540', 'Rua Aristóteles Martins', 'Casa', 83, 'Jd Balneário', 'Presidente Prudente', 'SP',
#      'jrfoliva@gmail.com', '(18) 99806-7041', 'junior', '123', 'adm', 1)

