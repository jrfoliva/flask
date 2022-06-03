
class Perfil(object):
    def __init__(self, perfil, consultar=0, incluir=0, alterar=0, excluir=0):
        self.__perfil = perfil
        self.__consultar = consultar
        self.__incluir = incluir
        self.__alterar = alterar
        self.__excluir = excluir

    # Métodos Get and Setter
    @property
    def perfil(self):
        return self.__perfil
    
    @perfil.setter
    def perfil(self, novoPerfil):
        self.__perfil = novoPerfil

    
    @property
    def consultar(self):
        return self.__consultar

    @consultar.setter
    def consultar(self, novoConsultar):
        self.__consultar = novoConsultar

    
    @property
    def incluir(self):
        return self.__incluir

    @incluir.setter
    def incluir(self, novoIncluir):
        self.__incluir = novoIncluir

    
    @property
    def alterar(self):
        return self.__alterar

    @alterar.setter
    def alterar(self, novoAlterar):
        self.__alterar = novoAlterar

    
    @property
    def excluir(self):
        return self.__excluir

    @excluir.setter
    def excluir(self, novoExcluir):
        self.__excluir = novoExcluir