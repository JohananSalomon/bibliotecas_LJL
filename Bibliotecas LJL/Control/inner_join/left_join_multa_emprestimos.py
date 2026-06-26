import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conecta

def left_join_multa_emprestimos():
    conn = conecta()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT 
            l.id_cliente,
            l.data_emprestimo,
            l.data_devolucao_prevista,
            l.status_emprestimo,
            c.valor
        FROM emprestimos l
        LEFT JOIN multas c ON l.id_emprestimo = c.id_emprestimo
    """)    
    resultados = cursor.fetchall()
    
    for i in resultados:

        print(i)
        
    cursor.close()
    conn.close()














































































































































