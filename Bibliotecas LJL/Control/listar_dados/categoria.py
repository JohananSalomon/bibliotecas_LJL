from conexao import conecta

def listar_categorias():
    conexao = conecta()
    cursor = conexao.cursor()
    cursor.execute("SELECT  FROM categorias")
    categorias = cursor.fetchall()

    for i in categorias:
        print(i)



