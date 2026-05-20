import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta

def cadastrar_livro_estoque():
    id_livro = int(input("ID do livro: "))
    quantidade_disponivel = int(input("Quantidade disponível: "))
    quantidade_reservada = int(input("Quantidade reservada: "))
    quantidade_total = int(input("Quantidade total: "))
    localizacao = input("Localização (ex: Prateleira A3): ")
    data_entrada = input("Data de entrada (AAAA-MM-DD): ")




    sql = """INSERT INTO estoque (id_livro, quantidade_disponivel, quantidade_reservada, quantidade_total, localizacao, data_entrada) 
             VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (id_livro, quantidade_disponivel, quantidade_reservada, quantidade_total, localizacao, data_entrada)

 

  
    conexao = conecta()
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("editoras cadastrada com sucesso! ")











