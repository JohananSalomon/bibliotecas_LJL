import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta
def left_join_livro_cliente():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT l.titulo, l.isbn, l.ano_publicacao, l.quantidade, l.idioma, l.numero_paginas, e.valor_unitario, e.observacao,e.status_item FROM livros l  left JOIN itens_emprestimo e ON e.id_livro = l.id_livro")
    categorias = cursor.fetchall()
    cursor.close()
    conn.close()

    for i in categorias:
        print(i)







