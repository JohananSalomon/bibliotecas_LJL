import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta

def cadastrar_emprestimos():
    id_cliente = input("ID do cliente: ")
    id_funcionario = input("ID do funcionário: ")
    data_emprestimo = input("Data do empréstimo (AAAA-MM-DD): ")
    data_devolucao_prevista = input("Data de devolução prevista (AAAA-MM-DD): ")
    data_devolucao_real = input("Data de devolução real (AAAA-MM-DD): ")
    status_emprestimo = input("Status do empréstimo: ")
    valor_multa = input("Valor da multa: ")







    sql = """
            INSERT INTO emprestimos (id_cliente, id_funcionario, data_emprestimo, data_devolucao_prevista, data_devolucao_real, status_emprestimo, valor_multa) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

    values = (id_cliente, id_funcionario, data_emprestimo, data_devolucao_prevista, data_devolucao_real, status_emprestimo, valor_multa)
    conexao = conecta()
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("Empréstimo cadastrado com sucesso!")

        
    

