from flask import Flask, request, jsonify
import produtos_dao
from sql_connection import get_sql_connection


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



if __name__ == "__main__":
    print("Iniciando o Flask Server para o Sistema de cervejaria")
    app.run(port=5000)