import mysql.connector
def conecta():
    global conexao
    #executa uma funçao da lib que realiza a conexao
    conexao = mysql.connector.connect(
        #parametro de conexao o banco de dados
        host ="localhost",
        user="root",
        password="",
        database = "biblioteca"
    )
    return conexao



