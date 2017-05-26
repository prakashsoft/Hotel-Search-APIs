from hotel_search.scrapers.common import Scraper


class ExpediaScraper(Scraper):

    provider = "Expedia"
    def load_results(self):
        self.load_fake_results(xrange(1, 200,5))
