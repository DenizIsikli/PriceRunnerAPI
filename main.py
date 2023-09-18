import BeautifulSoup.scraper as scraper
import CRUD.crud as crud


def main():
    api = scraper.PriceRunnerAPI()
    api.run()


if __name__ == '__main__':
    main()
