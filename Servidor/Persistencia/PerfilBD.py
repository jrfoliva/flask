from Modelo.Perfil import Perfil
import sqlite3

caminhoBancoDeDados = 'C:/DEV/Flask/ProjetoWeB/Servidor/Persistencia/dados/BancoDedados.db'

class PerfilBD(object):
    def __init__(self):
        self.__conexao = sqlite3.connect(caminhoBancoDeDados)
        with self.__conexao as con:
            cursor = con.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Perfil (
                    perfil varchar(30) NOT NULL,
                    consultar BOOLEAN,
                    incluir BOOLEAN,
                    alterar BOOLEAN,
                    excluir BOOLEAN,
                    CONSTRAINT pk_perfil
                        PRIMARY KEY (perfil)   
                )
            """)
            con.commit()


    def incluir(self, perfil):
        if isinstance(perfil, Perfil):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    INSERT INTO Perfil 
                    VALUES (?, ?, ?, ?, ?)
                    """, (perfil.perfil, perfil.consultar, perfil.incluir,
                    perfil.alterar, perfil.excluir)
                )
                con.commit()

    
    def alterar(self, perfil):
        if isinstance(perfil, Perfil):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    UPDATE Perfil SET perfil = ?, consultar = ?, incluir = ?
                        alterar = ?, excluir = ?
                    WHERE perfil = ?                        
                """, (perfil.perfil, perfil.consultar, perfil.incluir, perfil.alterar,
                    perfil.excluir, perfil.perfil)
                )
                con.commit()

    
    def apagar(self, perfil):
        if isinstance(perfil, Perfil):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    DELETE FROM Perfil
                    WHERE perfil = ?
                """, [perfil.perfil]
                )
                con.commit()


    def consultar(self, termo):
        with self.__conexao as con:
            cursor = con.cursor()
            cursor.execute("""
                SELECT * FROM Perfil
                WHERE perfil like ?
            """, [termo+"%"]
            )
            resultado = cursor.fetchall()
            if resultado:
                listaPerfil = []
                for item in resultado:
                    perfil = Perfil(item[0], item[1], item[2], item[3], item[4])
                    listaPerfil.append(perfil)
                return listaPerfil
            else:
                return []
