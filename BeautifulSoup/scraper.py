from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import random
import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

# Flask is running on http://127.0.0.1:5000/search/iphone


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

        self.url = None

        self.products = []

        self.name = None
        self.info = None
        self.price = None
        self.link = None

    def search_product(self, product_name):
        self.url = 'https://www.pricerunner.dk/search?q=' + product_name.replace(" ", "+")

        try:
            response = requests.get(self.url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                product_div = soup.find('div', class_='mIkxpLfxgo pr-1dtdlzd')

                if product_div:
                    for item_div in product_div.find_all('div', class_='pr-1k8dg1g'):
                        # Extract product information within each product's container
                        self.name = item_div.find('h3', class_='pr-z2tzuf').text
                        self.info = item_div.find('p', class_='pr-1qhwt5w').text
                        self.price = item_div.find('span', class_='pr-yp1q6p').text
                        self.price = self.price.replace('\xa0', '')
                        self.link = item_div.find('a')['href']

                        product_dict = {'name': self.name, 'info': self.info, 'price': self.price, 'link': self.link}
                        self.products.append(Product(**product_dict))
                        print(self.products)

                if soup.find('button', class_='pr-5cnc2s'):
                    return self.products

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

        return self.products

    def run(self):
        @self.app.route('/search/<product_name>')
        def search_route(product_name):
            products = self.search_product(product_name)

            return jsonify(products)

        self.app.run(debug=True)
