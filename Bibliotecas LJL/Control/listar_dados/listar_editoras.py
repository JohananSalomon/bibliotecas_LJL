import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conecta

def listar_editoras():
    conn = conecta()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_editoras, nome, cnpj, endereco, cidade, estado, telefone FROM editoras")
    resultados = cursor.fetchall()
    
    for i in resultados:
        print(i)
        
    cursor.close()
    conn.close()
