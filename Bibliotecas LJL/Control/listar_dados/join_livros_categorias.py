import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta
def join_livros_categorias():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT l.titulo, l.ano_publicacao, c.nome FROM categorias c INNER JOIN livros l ON c.id_categoria = l.id_categoria")
    categorias = cursor.fetchall()
    cursor.close()
    conn.close()

    for i in categorias:
        print(i)

join_livros_categorias()
