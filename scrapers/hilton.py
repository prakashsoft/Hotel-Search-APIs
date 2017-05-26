from hotel_search.scrapers.common import Scraper


class HiltonScraper(Scraper):

    provider = "Hilton"
    def load_results(self):
        self.load_fake_results(xrange(1, 300,1))
