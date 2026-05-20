import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta

def listar_clientes():
    conn = conecta()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_cliente, nome, cpf, data_nascimento, endereco, telefone, email, data_cadastro FROM clientes")
    resultados = cursor.fetchall()
    
    for i in resultados:
        print(i)
        
    cursor.close()
    conn.close()