import mysql.connector
from conexao import conecta
    

def categorias():
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
