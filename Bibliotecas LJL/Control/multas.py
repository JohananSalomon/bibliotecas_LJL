import mysql.connector
from conexao import conecta
    


def multas():
    id_emprestimo = input("ID do empréstimo: ")
    valor = input("Valor: ")
    motivo = input("Motivo: ")
    data_multa = input("Data da multa (AAAA-MM-DD): ")
    status_pagamento = input("Status do pagamento: ")
    data_pagamento = input("Data do pagamento (AAAA-MM-DD): ")
    observacoes = input("Observações: ")

    sql = """
            INSERT INTO multas (id_emprestimo, valor, motivo, data_multa, status_pagamento, data_pagamento, observacoes) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
    values = (id_emprestimo, valor, motivo, data_multa, status_pagamento, data_pagamento, observacoes)
    conexao = conecta()
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("Multa cadastrada com sucesso!")


