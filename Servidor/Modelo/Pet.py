class Pet(object):
    
    # construtor da classe Pet
    def __init__(self, codigo=0, nome="", especie="", raca="",
                        cor="", dataNasc="", numMicroChip="", rga=""):
        self.__codigo = codigo
        self.__nome = nome
        self.__especie = especie
        self.__raca = raca
        self.__cor = cor
        self.__dataNasc = dataNasc
        self.__numMicroChip = numMicroChip
        self.__rga = rga

    
    # método get
    @property
    def codigo(self):
        return self.__codigo

    #metodo setter
    @codigo.setter
    def codigo(self, novoCodigo):
        self.__codigo = novoCodigo


    @property
    def nome(self):
        return self.__nome
    
    #metodo setter
    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome


    @property
    def especie(self):
        return self.__especie
    
    #metodo setter
    @especie.setter
    def especie(self, novaEspecie):
        self.__especie = novaEspecie


    @property
    def raca(self):
        return self.__raca

    #metodo setter
    @raca.setter
    def raca(self, novaRaca):
        self.__raca = novaRaca

    
    @property
    def cor(self):
        return self.__cor
    
    #metodo setter
    @cor.setter
    def cor(self, novaCor):
        self.__cor = novaCor


    @property
    def dataNasc(self):
        return self.__dataNasc
   
    #metodo setter
    @dataNasc.setter
    def dataNasc(self, novadtNasc):
        self.__dataNasc = novadtNasc


    @property
    def numMicroChip(self):
        return self.__numMicroChip
    
    #metodo setter
    @numMicroChip.setter
    def numMicroChip(self, novoNumMicroChip):
        self.__numMicroChip = novoNumMicroChip


    @property
    def rga(self):
        return self.__rga
    
    #metodo setter
    @rga.setter
    def rga(self, novoRga):
        self.__rga = novoRga

    #override do método str
    def __str__(self):
        return (f'Código: {self.__codigo} | Nome: {self.__nome.title()} | Espécie: {self.__especie} | Raça: {self.__raca}'
            + f'| Cor: {self.__cor} | Dt. Nasc.: {self.__dataNasc} | Microchip: {self.__numMicroChip} | RGA: {self.__rga}' )