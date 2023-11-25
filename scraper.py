from flask import Flask, jsonify, request
from flask_restful import Api
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from database import Database


@dataclass
class Product:
    name: str = None
    info: str = None
    price: int = None
    link: str = None


class PriceRunnerAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.url = "https://www.pricerunner.dk"
        self.products = []
        self.port = 5000

        try:
            self.db = Database('Pricerunner.db')
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    @staticmethod
    def scrape_product_data(item_div):
        name_element = item_div.find('h3', class_='pr-c6rk6p')
        info_element = item_div.find('p', class_='pr-f6mg9h')
        price_element = item_div.find('span', class_='pr-yp1q6p')
        link_element = item_div.find('a')['href']

        # Extract product information in text format within each product's container
        name = name_element.text if name_element else None
        info = info_element.text if info_element else None
        price = price_element.text.replace('\xa0', '') if price_element else None
        link = f"https://www.pricerunner.dk{link_element}" if link_element else None

        return Product(name, info, price, link)

    def search_product(self, product_name):
        self.products = []
        search_url = f'{self.url}/search?q={product_name.replace(" ", "+")}'

        try:
            response = requests.get(search_url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                product_div = soup.find('div', class_='mIkxpLfxgo pr-1dtdlzd')

                if product_div:
                    for item_div in product_div.find_all('div', class_='pr-1k8dg1g'):
                        product = self.scrape_product_data(item_div)
                        self.products.append(Product(product.name, product.info, product.price, product.link))

                if soup.find('button', class_='pr-5cnc2s'):
                    pass

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

        return self.products

    def get_product_by_name(self, product_name):
        result = self.db.get_product_by_name(product_name)
        if result:
            return jsonify(result)
        return jsonify({'message': 'Product not found'}), 404

    def update_product_price(self, product_name, new_price):
        success = self.db.update_product_price(product_name, new_price)
        if success:
            return jsonify({'message': 'Product price updated successfully'})
        return jsonify({'message': 'Failed to update product price'}), 500

    def delete_product(self, product_name):
        success = self.db.delete_product(product_name)
        if success:
            return jsonify({'message': 'Product deleted successfully'})
        return jsonify({'message': 'Failed to delete product'}), 500

    def run(self):
        @self.app.route('/search/<product_name>')
        def search_route(product_name):
            try:
                # self.db.add_product(product)
                products = self.search_product(product_name)

                if products:
                    response_str = '\n'.join(f"{i+1}: {product}" for i, product in enumerate(products))
                    print(f"{response_str}\n")
                    return jsonify(products)
                else:
                    return jsonify({'message': 'No products found'}), 404

            except Exception as e:
                return jsonify({'error': str(e)}), 500

        @self.app.route('/products/<product_name>', methods=['GET', 'PUT', 'DELETE'])
        def product_operations(product_name):
            if request.method == 'GET':
                return self.get_product_by_name(product_name)

            elif request.method == 'PUT':
                new_price = request.json.get('price')  # Assume updating the price
                return self.update_product_price(product_name, new_price)

            elif request.method == 'DELETE':
                return self.delete_product(product_name)

            return jsonify({'error': 'Invalid request method'}), 405

        self.app.run(port=self.port, debug=True)
