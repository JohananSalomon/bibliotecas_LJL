import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta

def cadastrar_autores():
    nome = input("Nome do autor: ")
    nacionalidade = input("Nacionalidade: ")
    data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    biografia = input("Biografia: ")

    sql = """
            INSERT INTO autores (nome, nacionalidade, data_nascimento, email, telefone, biografia)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
    
    values = (nome, nacionalidade, data_nascimento, email, telefone, biografia)

  
    conexao = conecta()
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("autor cadastrado com sucesso!")
   




































































