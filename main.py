from scraper import PriceRunnerAPI
from database import Database


def main():
    # Initialize the API
    api = PriceRunnerAPI()

    # Initialize the database
    db = Database(
        database="mydatabase",
        user="myuser",
        password="mypassword",
        host="localhost",
        port="5432"
    )

    # Start the API
    api.run()

    # Don't forget to close the database connection
    db.close()


if __name__ == '__main__':
    main()
