import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conecta

def listar_itens_emprestimo():
    conn = conecta()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_emprestimo,id_livro,quantidade FROM itens_emprestimo")
    resultados = cursor.fetchall()
    
    for i in resultados:
        print(i)
        
    cursor.close()
    conn.close()

