from sql_connection import get_sql_connection

def get_all_products(connection):
    

    cursor = connection.cursor()

    query = "SELECT * FROM sistema_cervejaria.cerveja"

    cursor.execute(query)

    response = []

    for(id_cerveja, nome, estoque, valor) in cursor:
        response.append(
                    {
                        'id_cerveja' : id_cerveja, 
                        'nome' : nome, 
                        'estoque' : estoque, 
                        'valor' : valor
                    }
        )

    return response
if __name__=='__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))