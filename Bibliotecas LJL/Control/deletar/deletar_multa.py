import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta

def deletar_multa():
    id_del_multas = input("Qual funcionario deseja deletar?:")

    if id_del_multas == '':
        print("Digite uma opção válida!")
        return

    conexao = conecta()
    cursor = conexao.cursor()

    sql = "delete from multas where id_multa = '%s'" % (id_del_multas)  

    cursor.execute(sql) 

    conexao.commit()

    cursor.close()
    conexao.close()

    print ("multa deletado com sucesso!")