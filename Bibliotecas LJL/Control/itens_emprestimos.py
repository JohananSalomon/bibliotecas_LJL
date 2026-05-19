import mysql.connector
from conexao import conecta
    

def itens_emprestimo():
    id_emprestimo = input("ID do empréstimo: ")
    id_livro = input("ID do livro: ")
    quantidade = input("Quantidade: ")
    valor_unitario = input("Valor unitário: ")
    observacao = input("Observação: ")
    status_item = input("Status do item: ")

    sql = """
            INSERT INTO itens_emprestimo (id_emprestimo, id_livro, quantidade, valor_unitario, observacao, status_item) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """ 
    values = (id_emprestimo, id_livro, quantidade, valor_unitario, observacao, status_item)
    conexao = conecta()
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("Item de empréstimo cadastrado com sucesso!")
    

