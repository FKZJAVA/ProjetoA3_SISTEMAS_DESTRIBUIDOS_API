from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()

    query = "SELECT * FROM sistema_cervejaria.cerveja"

    cursor.execute(query)

    response = []

    for (id_cerveja, nome, estoque, valor) in cursor:
        response.append(
            {
                'id_cerveja': id_cerveja,
                'nome': nome,
                'estoque': estoque,
                'valor': valor
            }
        )

    return response


def insert_new_product(connection, cerveja):
    cursor = connection.cursor()
    query = ("INSERT INTO cerveja "
             "(nome, estoque, valor)"
             "VALUES (%s, %s, %s)")

    data = (cerveja['nome_cerveja'], cerveja['estoque'], cerveja['valor'])

    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, id_cerveja):
    cursor = connection.cursor()
    query = ("DELETE FROM cerveja where id_cerveja=" + str(id_cerveja))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid



if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 5))
    
    