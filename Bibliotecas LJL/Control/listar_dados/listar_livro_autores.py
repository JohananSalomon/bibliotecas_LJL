import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conecta

def listar_livro_autores():
    conn = conecta()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_autor,funcao_autor,data_vinculo,observacao FROM livro_autores")
    resultados = cursor.fetchall()
    
    for i in resultados:
        print(i)
        
    cursor.close()
    conn.close()

listar_livro_autores()