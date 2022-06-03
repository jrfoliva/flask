# Classe que comunicará com o banco de dados

# importações
from Modelo.Cliente import Cliente
import sqlite3

caminhoBancoDeDados = 'C:/DEV/Flask/ProjetoWeB/Servidor/Persistencia/dados/BancoDedados.db'

class ClienteBD(object):

    def __init__(self):
        self.__conexao = sqlite3.connect(caminhoBancoDeDados)
        with self.__conexao as con:
            cursor = con.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Cliente(
                    nome TEXT NOT NULL,
                    rg VARCHAR(12) NOT NULL,
                    cpf VARCHAR(14) NOT NULL UNIQUE,
                    dataNasc TEXT NULL,
                    cep TEXT NULL,
                    rua TEXT NULL,
                    num INTEGER NULL,
                    complemento TEXT NULL,
                    bairro TEXT NULL,
                    cidade TEXT NULL,
                    estado TEXT NULL,
                    telefone TEXT NULL,
                    email TEXT NULL,
                    CONSTRAINT pk_cliente
                        PRIMARY KEY (rg, cpf)
                )
            
            """)
            con.commit()


    def incluir(self, cliente):
        """Método para incluir registro na tabela cliente."""
        if isinstance(cliente, Cliente):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                        INSERT INTO Cliente (nome, rg, cpf, dataNasc, cep,
                            rua, num, complemento, bairro, cidade, estado, telefone, email)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (cliente.nome, cliente.rg, cliente.cpf, cliente.dataNasc,
                cliente.cep, cliente.rua, cliente.num, cliente.complemento, cliente.bairro,
                cliente.cidade, cliente.estado, cliente.telefone, cliente.email)
                )
                con.commit()


    def alterar(self, cliente):
        """Método que altera um registro recebendo uma instância de Cliente."""
        if isinstance(cliente, Cliente):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    UPDATE Cliente SET nome = ?, rg = ?, cpf =?, dataNasc = ?,
                        cep = ?, rua = ?, num = ?, complemento = ?, bairro = ?,
                        cidade = ?, estado = ?, telefone = ?, email = ?
                    WHERE cpf = ?
                """, (cliente.nome, cliente.rg, cliente.cpf, cliente.dataNasc,
                cliente.cep, cliente.rua, cliente.num, cliente.complemento, cliente.bairro,
                cliente.cidade, cliente.estado, cliente.telefone, cliente.email,
                cliente.cpf)
                )
                con.commit()


    def apagar(self, cliente):
        """Método que apaga um registro, recebendo como parâmetro uma instância de Cliente."""
        if isinstance(cliente, Cliente):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    DELETE FROM cliente 
                    WHERE cpf = ?
                """, ([cliente.cpf])
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
                        Select * From Cliente
                        Where cpf = ?
                    """, [termo]
                )
                resultado = cursor.fetchone()
            if resultado:
                cliente = Cliente(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4],
                        resultado[5], resultado[6], resultado[7], resultado[8], resultado[9], resultado[10], resultado[11],
                        resultado[12])
                return cliente
            else:
                return None
        else:  
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute(
                    """
                        Select * From Cliente
                        Where nome like ?
                    """, [termo+"%"]
                )
                resultados = cursor.fetchall()
            if resultados:    
                listaCliente = []
                for resultado in resultados:
                    cliente = Cliente(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4],
                        resultado[5], resultado[6], resultado[7], resultado[8], resultado[9], resultado[10], resultado[11],
                        resultado[12])
                    listaCliente.append(cliente)
                return listaCliente
            else:
                return []
