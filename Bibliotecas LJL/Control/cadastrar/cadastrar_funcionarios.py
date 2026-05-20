import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta
def cadastrar_funcionarios():
    nome = input("qual é o nome do funcionário que voce deseja cadastrar?:")
    cpf = input("Qual é o seu cpf?:")
    cargo = input("Qual é o seu cargo?:") 
    salario = input("Qual é o seu sálario?:")
    telefone = input("Qual é o seu telefone?:")
    email = input("Qual é o seu email?:")
    data_admissao = input("Qual é sua data de admissão (AAAA-MM-DD)?:")

    conn = conecta()
    cursor = conn.cursor()

    sql = "INSERT INTO funcionarios (nome, cpf, cargo, salario, telefone, email, data_admissao) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valores = (nome, cpf, cargo, salario, telefone, email, data_admissao)

    cursor.execute(sql, valores)
    conn.commit()

    print("Funcionário cadastrado com sucesso!")

    cursor.close()
    conn.close()

