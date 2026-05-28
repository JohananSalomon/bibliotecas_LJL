import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta
def join_livro_estoque():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT l.titulo, l.quantidade, c.id_estoque,c.localizacao FROM  c INNER JOIN livros l ON c.id_livro = l.id_livro")
    categorias = cursor.fetchall()
    cursor.close()
    conn.close()

    for i in categorias:
        print(i)

join_livro_estoque()












































































