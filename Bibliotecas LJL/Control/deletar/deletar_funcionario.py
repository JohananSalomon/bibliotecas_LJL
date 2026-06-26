import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta

def deletar_funcionario():
    id_del_funcionario = input("Qual funcionario deseja deletar?:")

    if id_del_funcionario == '':
        print("Digite uma opção válida!")
        return

    sql = "delete from funcionarios where id_funcionario = '%s'"
    conexao = conecta()
    cursor = conexao.cursor()
    cursor.execute(sql % (id_del_funcionario,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("funcionario deletado com sucesso!")