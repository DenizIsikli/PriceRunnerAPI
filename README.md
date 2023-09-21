# PriceRunnerAPI

PriceRunnerAPI is a RESTful API that allows you to search for products on the Danish version of PriceRunner and retrieve product information in a structured format.

## Base URL

The base URL for the PriceRunnerAPI is `https://www.example.com/api/`.

## Versioning

To ensure backward compatibility, the API is versioned. The current version is `v1`. You should specify the version in the URL when making requests.

## Authentication

Authentication is not required for most endpoints. However, some endpoints may require API key authentication in the future.

## Errors

The API uses standard HTTP status codes to indicate the success or failure of a request. Detailed error messages will be included in the response body.

## Endpoints

### Search for a Product

- **URL:** `/search/<product_name>`
- **Method:** GET
- **Description:** Searches for a product by name and returns a list of matching products.
- **Parameters:**
  - `product_name` (string): The name of the product to search for.

### Get a List of Products

- **URL:** `/products`
- **Method:** GET
- **Description:** Retrieves a list of all products.

### Create a New Product

- **URL:** `/products`
- **Method:** POST
- **Description:** Creates a new product entry.
- **Parameters:** JSON object with product details.

### Delete a Product

- **URL:** `/products/<product_id>`
- **Method:** DELETE
- **Description:** Deletes a product by its ID.
- **Parameters:**
  - `product_id` (integer): The ID of the product to delete.

This API is designed to provide easy access to product information from PriceRunner Denmark. You can use it to search for products, retrieve a list of products, create new product entries, and delete existing product entries. Enjoy exploring the world of products with PriceRunnerAPI!

For detailed usage instructions and examples, please refer to the [PriceRunnerAPI Documentation](Documentation.md).
