import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta

def cadastrar_clientes():
    nome = input("qual é o nome do cliente que voce deseja cadastrar?:")
    cpf = input("Qual é o seu cpf?:")
    data_nascimento = input("Qual é a sua data de nascimento (AAAA-MM-DD)?:")
    endereco = input("Qual é o seu endereço?:")
    telefone = input("Qual é o seu telefone?:")
    email = input("Qual é o seu email?:")

    conn = conecta()
    cursor = conn.cursor()

    sql = "INSERT INTO clientes (nome, cpf, data_nascimento, endereco, telefone, email) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (nome, cpf, data_nascimento, endereco, telefone, email)

    cursor.execute(sql, valores)
    conn.commit()

    print("Cliente cadastrado com sucesso!")

    cursor.close()
    conn.close()

    