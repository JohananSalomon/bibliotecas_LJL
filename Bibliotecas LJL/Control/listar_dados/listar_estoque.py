import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conecta

def listar_estoque():
    conn = conecta()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_livro,quantidade_disponivel,quantidade_reservada,quantidade_total,data_entrada FROM estoque")
    resultados = cursor.fetchall()
    
    for i in resultados:
        print(i)
        
    cursor.close()
    conn.close()

listar_estoque()