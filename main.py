from scraper import PriceRunnerAPI
from database import Database

def main():
    # Initialize the API
    api = PriceRunnerAPI()

    # Start the API
    api.run()

if __name__ == '__main__':
    main()
