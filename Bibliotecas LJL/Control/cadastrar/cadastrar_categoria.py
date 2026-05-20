import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta
    

def cadastrar_categoria():
    nome = input("Nome da categoria: ")
    descricao = input("Descrição: ")
    codigo = input("Código: ")
    setor = input("Setor: ")

    sql = """
            INSERT INTO categorias (nome, descricao, codigo, setor) 
            VALUES (%s, %s, %s, %s)
        """
    values = (nome, descricao, codigo, setor)
    conexao = conecta()
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("Categoria cadastrada com sucesso!")

