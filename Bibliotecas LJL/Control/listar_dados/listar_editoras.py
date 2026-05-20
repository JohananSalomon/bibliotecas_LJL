import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conecta

def listar_editoras():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM editoras")
    editoras = cursor.fetchall()
    cursor.close()
    conn.close()

    for i in editoras:
        print(i)
    
