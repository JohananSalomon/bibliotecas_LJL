import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta

def  listar_multas():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM multas")
    multas = cursor.fetchall()
    conn.close()
    
    for i in multas:
        print(i)



















