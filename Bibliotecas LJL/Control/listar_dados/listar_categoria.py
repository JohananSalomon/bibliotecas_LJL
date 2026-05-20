import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta
def listar_categorias():
    conexao = conecta()
    cursor = conexao.cursor()
    cursor.execute("SELECT  FROM categorias")
    categorias = cursor.fetchall()

    for i in categorias:
        print(i)



