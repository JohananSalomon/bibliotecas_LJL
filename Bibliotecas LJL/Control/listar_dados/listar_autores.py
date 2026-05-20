import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta
def listar_autores():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT id_autor, nome, nacionalidade, data_nascimento, email, telefone, biografia FROM autores")
    autores = cursor.fetchall()
    cursor.close()
    conn.close()

    for i in autores:
        print(i)
