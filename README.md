# PriceRunnerAPI

PriceRunnerAPI is a Flask-based RESTful API designed to facilitate searching for products on the Danish version of PriceRunner. It retrieves product information in a structured format.

## Installation and Setup

To run the PriceRunnerAPI, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/pricerunner-api.git
    ```

2. Install dependencies:

    ```bash
    cd pricerunner-api
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

## Usage

The PriceRunnerAPI exposes several endpoints for product-related operations:

### Search for a Product

- **URL:** `/search/<product_name>`
- **Method:** GET
- **Description:** Searches for a product by name and returns a list of matching products.
- **Parameters:**
  - `product_name` (string): The name of the product to search for.

### Get Product Information

- **URL:** `/products/<product_name>`
- **Methods:** GET, PUT, DELETE
- **Description:** Perform operations on a specific product.
  - `GET`: Retrieve details of a product by its name.
  - `PUT`: Update the price of a product by providing a new price in the request body (JSON format).
  - `DELETE`: Delete a product by its name.

## Database Integration

The PriceRunnerAPI integrates with a SQLite database named `Pricerunner.db` to store and manage product information.

## Dependencies

- Flask: Web framework for building the API.
- Flask-RESTful: Extension for creating REST APIs with Flask.
- Requests: Library for making HTTP requests.
- BeautifulSoup: For web scraping and parsing HTML data.
- Dataclasses: Provides a decorator for quickly defining classes with a set of fields.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
