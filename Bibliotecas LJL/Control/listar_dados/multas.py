from conexao import conecta

def  listar_multas():
    conn = conecta()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM multas")
    multas = cursor.fetchall()
    conn.close()
    
    for i in multas:
        print(i)



















