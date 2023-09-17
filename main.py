from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import random
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    info: str
    price: int
    link: str


class PriceRunnerAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)

        self.url = None

    def search_product(self, product_name):
        self.url = 'https://www.pricerunner.dk/search?q=' + product_name.replace(" ", "+")

        try:
            products = []

            response = requests.get(self.url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                product_div = soup.find('div', class_='mIkxpLfxgo pr-lt04mx')

                if product_div:
                    for item_div in product_div.find_all('div', class_='pr-1k8dg1g'):
                        # Extract product information within each product's container
                        name_product = item_div.find('h3', class_='pr-z2tzuf').text
                        info = item_div.find('p', class_='pr-1qhwt5w').text
                        price = item_div.find('span', class_='pr-yp1q6p').text
                        link = item_div.find('a')['href']

                        product = Product(name=name_product, info=info, price=price, link=link)
                        products.append(product)

                    if soup.find('button', class_='pr-5cnc2s'):
                        return

            return products

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def run(self):
        @self.app.route('/search/<product_name>')
        def search_route(product_name):
            products = self.search_product(product_name)
            product_dicts = [{'name': product.name, 'info': product.info, 'price': product.price, 'link': product.link}
                             for product in products]

            print(product_dicts)
            return jsonify(product_dicts)

        self.app.run(debug=True)


if __name__ == '__main__':
    api = PriceRunnerAPI()
    api.run()
