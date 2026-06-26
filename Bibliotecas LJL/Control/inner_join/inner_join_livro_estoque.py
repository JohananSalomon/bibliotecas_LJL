import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta
def inner_join_livro_estoque():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("create view livro_estoque as SELECT l.titulo, l.quantidade, c.id_estoque,c.localizacao FROM estoque c INNER JOIN livros l ON c.id_livro = l.id_livro")
    conn.commit()   
    cursor.execute("SELECT * FROM livro_estoque")
    categorias = cursor.fetchall()
    cursor.close()
    conn.close()

    for i in categorias:
        print(i)

join_livro_estoque()












































































