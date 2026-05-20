

import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))   
from conexao import conecta

def cadastrar_editora():
    nome = input("Nome da editora: ")
    cnpj = input("CNPJ: ")
    endereco = input("Endereço: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    telefone = input("Telefone: ")


    sql = "INSERT INTO editoras (nome, cnpj, endereco, cidade, estado, telefone) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (nome, cnpj, endereco, cidade, estado, telefone)       
    
 

  
    conexao = conecta()
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("editoras cadastrada com sucesso! ")
   



















































































