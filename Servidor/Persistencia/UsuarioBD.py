from Modelo.Usuario import Usuario
import sqlite3

caminhoBancoDeDados = 'C:/DEV/Flask/ProjetoWeB/Servidor/Persistencia/dados/BancoDedados.db'

class ClienteBD(object):

    def __init__(self):
        self.__conexao = sqlite3.connect(caminhoBancoDeDados)
        with self.__conexao as con:
            cursor = con.cursor()
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS Usuario (
                        nome varchar(50) NOT NULL,
                        rg varchar(12) NOT NULL,
                        cpf varchar(14) NOT NULL,
                        dtNasc varchar(10) NOT NULL,
                        cep varchar(9) NOT NULL,
                        endereco varchar(50) NOT NULL,
                        numero INTEGER NOT NULL,
                        complemento varchar(50) NULL,
                        bairro varchar(50) NOT NULL,
                        cidade varchar(50) NOT NULL,
                        uf varchar(2) NOT NULL,
                        email varchar(50) NULL,
                        telefone varchar(15) NULL,
                        login varchar(50) NOT NULL,
                        senha varchar(50) NOT NULL,
                        perfil varchar(30) NULL,
                        ativo BOOLEAN,
                        CONSTRAINT pk_usuario
                            PRIMARY KEY (rg, cpf, login),
                        CONSTRAINT fk_usuario_perfil
                            FOREIGN KEY (perfil)
                                REFERENCES Perfil (perfil)
                    )
                """)
            con.commit()

    def incluir(self, usuario):
        """Método para incluir registro na tabela Usuario."""
        if isinstance(usuario , Usuario):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                        INSERT INTO Usuario (nome, rg, cpf, dtNasc, cep, endereco, numero,
                             complemento, bairro, cidade, uf, email, telefone, login,
                                senha, perfil, ativo)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (usuario.nome, usuario.rg, usuario.cpf, usuario.dtNasc,
                usuario.cep, usuario.endereco, usuario.numero, usuario.complemento, usuario.bairro,
                usuario.cidade, usuario.estado, usuario.email, usuario.numTelefone, usuario.login,
                usuario.senha, usuario.perfil, usuario.ativo)
                )
                con.commit()


    def alterar(self, usuario):
        """Método que altera um registro recebendo uma instância de Usuario."""
        if isinstance(usuario, Usuario):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    UPDATE Usuario SET nome = ?, rg = ?, cpf =?, dtNasc = ?,
                        cep = ?, endereco = ?, numero = ?, complemento = ?, bairro = ?,
                        cidade = ?, uf = ?, email = ?, telefone = ?, login = ?, senha = ?,
                        perfil = ?, ativo = ?
                    WHERE cpf = ?
                """, (usuario.nome, usuario.rg, usuario.cpf, usuario.dtNasc,
                usuario.cep, usuario.endereco, usuario.numero, usuario.complemento, usuario.bairro,
                usuario.cidade, usuario.estado, usuario.email, usuario.numTelefone, usuario.login,
                usuario.senha, usuario.perfil, usuario.ativo, usuario.cpf)
                )
                con.commit()


    def apagar(self, usuario):
        """Método que apaga um registro, recebendo como parâmetro uma instância de Cliente."""
        if isinstance(usuario, Usuario):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    DELETE FROM Usuario 
                    WHERE cpf = ?
                """, ([usuario.cpf])
                )
                con.commit()

    
    def consultar(self, termo):
        """Método que retorna um registro ou uma instância de Cliente ou uma lista de Cliente 
           conforme o termo solicitado por parâmetro."""
        
        if termo[0:3].isdigit():  # procurando se há digitos para buscar por CPF
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute(
                    """
                        Select * From Usuario
                        Where cpf = ?
                    """, [termo]
                )
                resultado = cursor.fetchone()
            if resultado:
                usuario = Usuario(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4],
                        resultado[5], resultado[6], resultado[7], resultado[8], resultado[9], resultado[10], resultado[11],
                        resultado[12], resultado[13], resultado[14], resultado[15], resultado[16])
                return usuario
            else:
                return None
        else:  # implementação futura para busca por nome.
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute(
                    """
                        Select * From Usuario
                        Where nome like ?
                    """, [termo+"%"]
                )
                resultados = cursor.fetchall()
            if resultados:    
                listaUsuarios = []
                for resultado in resultados:
                    usuario = Usuario(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4],
                        resultado[5], resultado[6], resultado[7], resultado[8], resultado[9], resultado[10], resultado[11],
                        resultado[12], resultado[13], resultado[14], resultado[15], resultado[16])
                    listaUsuarios.append(usuario)
                return listaUsuarios
            else:
                return []
