import mysql.connector
from conexao import conecta
    
    
def cadastrar_livro():
    titulo = input("Título do livro: ")
    isbn = input("ISBN: ")  # string, não int
    ano_publicacao = int(input("Ano de publicação: "))
    quantidade = int(input("Quantidade em estoque: "))
    idioma = input("Idioma: ")
    numero_paginas = int(input("Número de páginas: "))
    id_editora = int(input("ID da editora: "))
    id_categoria = int(input("ID da categoria: "))


   
    sql = """
        INSERT INTO livros (titulo, isbn, ano_publicacao, quantidade, idioma, numero_paginas, id_editora, id_categoria)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (titulo, isbn, ano_publicacao, quantidade, idioma, numero_paginas, id_editora, id_categoria)

  
    conexao = conecta()
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("Livro cadastrado com sucesso!")
   

















