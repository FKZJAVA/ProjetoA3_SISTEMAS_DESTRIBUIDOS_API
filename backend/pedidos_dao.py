from datetime import datetime
from sql_connection import get_sql_connection
from decimal import Decimal



def insert_order(connection, pedido):
    cursor = connection.cursor()
    order_query = ("INSERT INTO pedido"
                   "(cliente_nome, data_pedido)"
                   "VALUES (%s,%s)")
    order_data = (pedido['cliente_nome'], datetime.now())

    cursor.execute(order_query,order_data)
    id_pedido = cursor.lastrowid

    order_details_query = ("INSERT INTO detalhes_pedido"
                           "(id_pedido, id_cerveja, quantidade, total)"
                           "VALUES (%s, %s, %s, %s)")
    

    order_details_data = []

    for order_detail_record in pedido['detalhes_pedido']:
        order_details_data.append((
            id_pedido,
            int(order_detail_record['id_cerveja']),
            int(order_detail_record['quantidade']),
            Decimal(order_detail_record['total'])
            
        ))

    cursor.executemany(order_details_query, order_details_data)    
    connection.commit()


    return id_pedido


def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM pedido")
    cursor.execute(query)

    response = []
    for (id_pedido, cliente_nome, data_pedido) in cursor:
        response.append({
            'id_pedido':id_pedido,
            'cliente_nome':cliente_nome,
            'data_pedido':data_pedido

        })

    return response    









if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))