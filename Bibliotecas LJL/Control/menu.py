import mysql.connector
import os
import sys 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexao import conecta
sys.path.append("Control/cadastrar")
sys.path.append("Control/listar_dados")

from cadastrar_autores import cadastrar_autores
from listar_autores import listar_autores
from cadastrar_categoria import cadastrar_categoria
from listar_categorias import listar_categorias
from cadastrar_cliente  import cadastrar_clientes
from listar_clientes import listar_clientes
from cadastrar_editoras import cadastrar_editora
from listar_editoras import listar_editoras
from cadastrar_emprestimos import cadastrar_emprestimos
from listar_emprestimos import listar_emprestimos
from cadastrar_funcionarios import cadastrar_funcionarios
from listar_funcionarios import listar_funcionarios
from cadastrar_livro_autores import cadastrar_livro_autor
from listar_livro_autores import listar_livro_autores
from cadastrar_livro_estoque import cadastrar_livro_estoque
from listar_livro_estoque import listar_livro_estoque
from cadastrar_livros import cadastrar_livros
from listar_livros import listar_livros
from cadastrar_multas import cadastrar_multas
from listar_multas import listar_multas
from cadastrar_itens_emprestimos import cadastrar_itens_emprestimos
from listar_itens_emprestimo import listar_itens_emprestimo






def menu ():
    while True:
        print("1 - cadastrar")
        print("2 - Listar")
        print("3 - Sair")
        opcao = input("escolha uma opção: ") 

        if opcao == "1":
            subcadastrar()
        elif opcao == "2":
            sublistar()
        elif opcao == "3":
            print("saindo...")
            break
        else:
            print("\nopção invalida!\n")
        

def subcadastrar():
    while True:
        print("== Cadastrar dados ==\n")
        print("1 - cadastrar autores")
        print("2 - cadastrar categoria")
        print("3 - cadastrar cliente")
        print("4 - cadastrar editoras")
        print("5 - cadastrar emprestimos")
        print("6 - cadastrar funcionarios")
        print("7 - cadastrar intens emprestimos")
        print("8 - cadastrar livro autores")
        print("9 - cadastrar estoque de livros")
        print("10 - cadastrar livros")
        print("11 - cadastrar multas")
        print("12 - ir ao menu principal")       
        opcao = input("\nEscolha!:")

        if opcao == "1":
            cadastrar_autores()

        elif opcao == "2":
            cadastrar_categoria()

        elif opcao == "3":
            cadastrar_clientes()

        elif opcao == "4":
            cadastrar_editora()

        elif opcao == "5":
            cadastrar_emprestimos()

        elif opcao == "6":
            cadastrar_funcionarios()

        elif opcao == "7":
            cadastrar_itens_emprestimos()

        elif opcao == "8":
            cadastrar_livro_autor()

        elif opcao == "9":
            cadastrar_livro_estoque()

        elif opcao == "10":
            cadastrar_livros()

        elif opcao == "11":
            cadastrar_multas()

        elif opcao == "12":
            print("voltando ao menu principal")
            break

        else:
            print ("\nopção invalida!\n")

def sublistar():
    while True:
        print("== Listar dados ==\n")
        print("1 - listar autores")
        print("2 - listar categoria")
        print("3 - listar cliente")
        print("4 - listar editoras")
        print("5 - listar emprestimos")
        print("6 - listar funcionarios")
        print("7 - listar intens emprestimos")
        print("8 - listar livro autores")
        print("9 - listar estoque de livros")
        print("10 - listar livros")
        print("11 - listar multas")
        print("12 - ir ao menu principal")       
        opcao = input("\nEscolha!:")

        if opcao == "1":
            listar_autores()

        elif opcao == "2":
            listar_categorias()

        elif opcao == "3":
            listar_clientes()

        elif opcao == "4":
            listar_editoras()

        elif opcao == "5":
            listar_emprestimos()

        elif opcao == "6":
            listar_funcionarios()

        elif opcao == "7":
            listar_itens_emprestimo()

        elif opcao == "8":
            listar_livro_autores()

        elif opcao == "9":
            listar_livro_estoque()

        elif opcao == "10":
            listar_livros()

        elif opcao == "11":
            listar_multas()

        elif opcao == "12":
            print("voltando ao menu principal")
            break

        else:
            print ("\nopção invalida!\n")

menu()