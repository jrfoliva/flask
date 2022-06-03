#As classes armazenadas na pasta Persistencia possuirão a responsabilidade
#de se comunicar com o banco de dados

from Modelo.Pet import Pet
import sqlite3

caminhoBancoDeDados = 'C:/DEV/Flask/ProjetoWeB/Servidor/Persistencia/dados/BancoDedados.db'

class PetBD(object):
    
    def __init__(self):
        self.__conexao = sqlite3.connect(caminhoBancoDeDados)
        with self.__conexao as con:
            cursor = con.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Pet (
                    codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    nome TEXT NOT NULL,
                    especie TEXT NOT NULL,
                    raca TEXT NOT NULL,
                    cor TEXT NOT NULL,
                    dataNasc TEXT NOT NULL,
                    numMicrochip TEXT NULL,
                    rga TEXT NOT NULL
                )
            """)
            con.commit()
    
    def incluir(self, pet):
        if isinstance(pet, Pet):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute(""" 
                    INSERT INTO Pet(nome, especie, raca, cor, dataNasc, numMicrochip, rga)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                
                """, (pet.nome, pet.especie, pet.raca, pet.cor, pet.dataNasc, pet.numMicroChip, pet.rga)
                )
                pet.codigo = cursor.lastrowid
                con.commit()

    def alterar(self, pet):
        if isinstance(pet, Pet):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    UPDATE Pet SET nome = ?, especie = ?, raca = ?, cor = ?, dataNasc = ?,
                    numMicrochip = ?, rga = ? WHERE codigo = ?
                """, (pet.nome, pet.especie, pet.raca, pet.cor, pet.dataNasc, pet.numMicroChip, pet.rga, pet.codigo))
                con.commit()


    def apagar(self, pet):
        if isinstance(pet, Pet):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    DELETE FROM Pet WHERE codigo = ?
                """, [pet.codigo])
                con.commit()


    def consultar(self, termo):
        if isinstance(termo, int):
            # Consultado pelo código do Pet
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                    SELECT codigo, nome, especie, raca, cor, dataNasc, numMicrochip, rga FROM Pet
                    WHERE codigo = ?
                """, [termo])
                resultado = cursor.fetchone() # retorno de apenas um registro do BD
                if resultado:
                    pet = Pet(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4],
                            resultado[5], resultado[6], resultado[7])
                    return pet
                else:
                    return None
        elif isinstance(termo, str):
            with self.__conexao as con:
                cursor = con.cursor()
                cursor.execute("""
                   SELECT codigo, nome, especie, raca, cor, dataNasc, numMicrochip, rga FROM Pet
                   WHERE nome like ?
                """,['%' + termo + '%'] )
                resultados = cursor.fetchall()
                listaPets = []
                for resultado in resultados:
                    pet = Pet(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4],
                            resultado[5], resultado[6], resultado[7])
                    listaPets.append(pet)
                return listaPets
        else:
            return None