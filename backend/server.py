from flask import Flask, request, jsonify
import produtos_dao
import pedidos_dao
from sql_connection import get_sql_connection
import json


app = Flask (__name__)

connection = get_sql_connection()

@app.route('/getProducts' , methods=['GET'])
def get_products():
    products = produtos_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = produtos_dao.delete_product(connection, request.form['id_cerveja'])
    response = jsonify({
        'id_cerveja': return_id


    })
    response.headers.add('Acess-Control-Allow-Origin', '*')
    return response


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    id_pedido = pedidos_dao.insert_order(connection, request_payload)
    response = jsonify({
        'id_pedido':id_pedido
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = pedidos_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Acess-Control-Allow-Origin', '*')
    return response




@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    id_cerveja = produtos_dao.insert_new_product(connection,request_payload)
    response = jsonify({
        'id_cerveja' : id_cerveja
    })
    response.headers.add('Acess-Control-Allow-Origin', '*')
    return response



if __name__ == "__main__":
    print("Iniciando o Flask Server para o Sistema de cervejaria")
    app.run(port=5000)