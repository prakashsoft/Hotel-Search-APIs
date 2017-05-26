from hotel_search.scrapers.common import Scraper


class PricelineScraper(Scraper):

    provider = "Priceline"
    def load_results(self):
        self.load_fake_results(xrange(1, 100,2))
