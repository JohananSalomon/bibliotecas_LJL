import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conecta

def listar_emprestimos():
    conn = conecta()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_cliente,id_funcionario,data_emprestimo,data_devolucao_prevista,data_devolucao_real,status_emprestimo,valor_multa FROM emprestimos")
    resultados = cursor.fetchall()
    
    for i in resultados:
        print(i)
        
    cursor.close()
    conn.close()

listar_emprestimos()