
import mysql.connector
from conexao import conecta
    


def cadastrar_livro_autor():
    id_livro = int(input("ID do livro: "))
    id_autor = int(input("ID do autor: "))
    funcao_autor = input("Função do autor (ex: escritor, tradutor): ")
    data_vinculo = input("Data de vínculo (AAAA-MM-DD): ")
    observacao = input("Observação: ")
    ativo = int(input("Ativo? (1 para sim, 0 para não): "))




    sql = """INSERT INTO livro_autores (id_livro, id_autor, funcao_autor, data_vinculo, observacao, ativo) 
             VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (id_livro, id_autor, funcao_autor, data_vinculo, observacao, ativo)


 

  
    conexao = conecta()
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("editoras cadastrada com sucesso! ")
   










