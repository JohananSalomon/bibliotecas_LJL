import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conecta

def listar_livros():
    conn = conecta()
    cursor = conn.cursor()
    
    cursor.execute("SELECT titulo,isbn,ano_publicacao,quantidade,idioma,numero_paginas FROM livros")
    resultados = cursor.fetchall()
    
    for i in resultados:
        print(i)
        
    cursor.close()
    conn.close()

listar_livros()