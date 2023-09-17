from flask import Flask, request, jsonify

app = Flask(__name__)

products = []


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    products.append(data)
    return jsonify(data), 201


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id < len(products):
        deleted_product = products.pop(product_id)
        return jsonify(deleted_product), 200
    else:
        return '', 404


if __name__ == '__main__':
    app.run(debug=True)
