import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conecta

def listar_funcionarios():
    conn = conecta()
    cursor = conn.cursor()
    
    cursor.execute("SELECT nome,cargo,telefone,email FROM funcionarios")
    resultados = cursor.fetchall()
    
    for i in resultados:
        print(i)
        
    cursor.close()
    conn.close()

listar_funcionarios()